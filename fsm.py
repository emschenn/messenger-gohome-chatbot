from transitions.extensions import GraphMachine
from utils import *
from gogo import *

class TocMachine(GraphMachine):

    def __init__(self,**machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
    def is_going_to_start(self, event):
        if event.get("message"):
            text = event['message']['text']
            return True
        return False
    def on_enter_start(self, event):
        print("I'm entering state1")
        sender_id = event['sender']['id']
#        responese = send_text_message(sender_id,"Hello！我是幫助你快速查詢家和學校兩地往訪之即時車次時刻的聊天機器人～")
        send_postback(sender_id)
        self.go_back()
    def on_exit_start(self):
        print('Leaving state1')


    def is_going_to_settrans(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text == "設定"
        if event.get("message"):
            text = event['message']['text']
            return text == "設定"
        return False
    def on_enter_settrans(self, event):
        print("I'm entering state2")
        #global set_flag = 1
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請輸入搭乘之交通工具\n（高鐵or火車）")
       # self.go_back()
    def on_exit_settrans(self, event):
        print('Leaving state2')

    def is_going_to_sethome(self, event):
        if event.get("message"):
            text = event['message']['text']
            return savetrans(text)
        return False
    def on_enter_sethome(self, event):
        print("I'm entering state2")
        #global set_flag = 1
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請輸入你家的站名")
       # self.go_back()
    def on_exit_sethome(self, event):
        print('Leaving state2')

    def is_going_to_setschool(self, event):
        if event.get("message"):
            text = event['message']['text']
            return savehome(text)
        return False
    def on_enter_setschool(self, event):
        print("I'm entering state2")
        #global set_flag = 1
        sender_id = event['sender']['id']
        send_text_message(sender_id, "請輸入你學校的站名")
       # self.go_back()
    def on_exit_setschool(self, event):
        print('Leaving state2')

    def is_going_to_done(self, event):
        if event.get("message"):
            text = event['message']['text']
            return saveschool(text)
        return False
    def on_enter_done(self, event):
        print("I'm entering state2")
        #global set_flag = 1
        sender_id = event['sender']['id']
        send_text_message(sender_id, "設定成功！")
       # send_generic_message(sender_id,show_button())
        self.go_back()
    def on_exit_done(self):
        print('Leaving state2')

    def is_going_to_goHome(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text == "回家"
        if event.get("message"):
            text = event['message']['text']
            return text == "回家"
        return False
    def on_enter_goHome(self, event):
        print("I'm entering state3")
        sender_id = event['sender']['id']
        send_text_message(sender_id,search("回家"))
        self.go_back()
    def on_exit_goHome(self):
        print('Leaving state3')


    def is_going_to_toSchool(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text == "回學校"
        if event.get("message"):
            text = event['message']['text']
            return text == "回學校"
        return False
    def on_enter_toSchool(self, event):
        print("I'm entering state4")
        sender_id = event['sender']['id']
        send_text_message(sender_id,search("回學校"))
        self.go_back()
    def on_exit_toSchool(self):
        print('Leaving state4')


