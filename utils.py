import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
#"EAAjhZBuIzJYoBAHhtYTv2XQZAE5eZBEmTBODJSeLx2wvmK4ti3RqhoHQOkBQGfHMhP9YtMcZCeHIIyflNb0wU18LZA9Psi1OeEvrilxsZA5ZBcXPCgdlTK0yR63Wo6wlxzVN7Hur0CKXJrSZCSQZBTMDArKzi7cMXcAqIGljwq6pGIwZDZD"

def send_postback(id):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL,ACCESS_TOKEN)
    payload = {
        "recipient":{"id":id},
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"Hello！我是幫助你快速查詢家和學校兩地往訪之車次時刻的聊天機器人～",
                    "buttons":[
                        {
                            'type':'postback',
                            'title':"設定",
                            'payload':"設定"
                        },
                        {
                            'type':'postback',
                            'title':"回家",
                            'payload':"回家"
                        },
                        {
                            'type':'postback',
                            'title':"回學校",
                            'payload':"回學校"
                        }
                   ]
                }
            }
        }
    }
    response = requests.post(url,json = payload)
    if response.status_code != 200:
        print("unable to send msg:" + response.text)
    return response

def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
