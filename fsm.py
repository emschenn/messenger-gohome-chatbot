from transitions.extensions import GraphMachine
from utils import send_text_message
from gogo import *

class TocMachine(GraphMachine):

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "開始"
        return False
    def on_enter_state1(self, event):
        print("I'm entering state1")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"Hello！我是幫助你快速查詢家和學校兩地往訪之車次時刻的聊天機器人～請先依照下列格式做初始設定ㄛ：）\nex:\n高雄（輸入你家的站）\n台南（輸入你學校的站）\n火車（搭乘高鐵/火車）")
        self.go_back()
    def on_exit_state1(self):
        print('Leaving state1')


    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return savedata(text)
        return False
    def on_enter_state2(self, event):
        print("I'm entering state2")
        #global set_flag = 1
        sender_id = event['sender']['id']
        send_text_message(sender_id, "設定成功！\n查詢回家車次請輸入：回家\n回學校車次請輸入：回學校\n重新設定請再次輸入：開始")
        self.go_back()
    def on_exit_state2(self):
        print('Leaving state2')


    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "回家"
        return False
    def on_enter_state3(self, event):
        print("I'm entering state3")
        sender_id = event['sender']['id']
        send_text_message(sender_id,search("回家"))
        self.go_back()
    def on_exit_state3(self):
        print('Leaving state3')


    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "回學校"
        return False
    def on_enter_state4(self, event):
        print("I'm entering state4")
        sender_id = event['sender']['id']
        send_text_message(sender_id,search("回學校"))
        self.go_back()
    def on_exit_state4(self):
        print('Leaving state4')

