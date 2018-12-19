from bottle import Bottle,route, run, request, abort, static_file

from fsm import TocMachine
import os

app = Bottle()
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PORT = os.environ['PORT']
#VERIFY_TOKEN = "emschenn"
machine = TocMachine(
    states=[
        'user',
        'start', #start
        'settrans', #setting
        'sethome',
        'setschool',
        'done',
	'goHome', #go home
	'toSchool', #go school
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'start',
            'conditions': 'is_going_to_start'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'settrans',
            'conditions': 'is_going_to_settrans'
        },
	{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'goHome',
            'conditions': 'is_going_to_goHome'
        },
	{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'toSchool',
            'conditions': 'is_going_to_toSchool'
        },
        {
            'trigger': 'advance',
            'source': 'settrans',
            'dest': 'sethome',
            'conditions': 'is_going_to_sethome'
        },
        {
            'trigger': 'advance',
            'source': 'sethome',
            'dest': 'setschool',
            'conditions': 'is_going_to_setschool'
        },
        {
            'trigger': 'advance',
            'source': 'setschool',
            'dest': 'done',
            'conditions': 'is_going_to_done'
        },
        {
            'trigger': 'go_back',
            'source': [
                'toSchool',
                'goHome',
                'done',
                'start'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@app.route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)

@app.route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
