import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import re
import sqlite3


#fromstation = "台南"
#tostation = "高雄"
def transform(station):
    if station == "台北" or station == "臺北": 
        return "1008"
    elif station == "板橋" :
        return "1011"
    elif station == "桃園" :
        return "1015"
    elif station == "新竹" :
        return "1025"
    elif station == "苗栗" :
        return "1305"
    elif station == "豐原" :
        return "1317"
    elif station == "台中" or station == "臺中" :
        return "1319"
    elif station == "彰化" :
        return "1120"
    elif station == "員林" :
        return "1203"
    elif station == "集集" :
        return "2705"
    elif station == "斗六" :
        return "1210"
    elif station == "斗南" :
        return "1211"
    elif station == "嘉義" :
        return "1215"
    elif station == "新營" :
        return "1220"
    elif station == "永康" :
        return "1227"
    elif station == "台南" or station == "臺南":
        return "1228"
    elif station == "岡山" :
        return "1233"
    elif station == "新左營" :
        return "1242"
    elif station == "高雄" :
        return "1238"
    elif station == "鳳山" :
        return "1402"
    elif station == "屏東" :
        return "1406"
    elif station == "枋寮" :
        return "1418"
    elif station == "台東" or station == "臺東" :
        return "1632"
    elif station == "花蓮" :
        return "1715"
    elif station == "羅東" :
        return "1823"
    elif station == "宜蘭" :
        return "1820"
    else:
        return "0"

def savedata(a):
    b = a.splitlines()
    if len(b) != 3:
        return False
    if transform(b[0]) == 0:
        return False
    if transform(b[1]) == 0:
        return False
    if b[2] == "火車" or b[2] == "客運":
       print("data correct")
    else:
       return False
    conn = sqlite3.connect('user')
    c = conn.cursor()
    c.execute('REPLACE INTO setting VALUES(?,?,?,?)',(1,b[0],b[1],b[2]))
    conn.commit()
    return True

#a = "台南\n高雄\n火車"
#savedata(a)


def to_matrix(l,n):
    return [l[i:i+n] for i in range(0,len(l),n)]

def trainsearch(a):
    conn = sqlite3.connect('user')
    c = conn.cursor()
    c.execute('SELECT * FROM setting')
    d = c.fetchone()
    if a == "回家":
        fromstation = d[2]
        tostation = d[1]
    elif a == "回學校":
        fromstation = d[1]
        tostation = d[2]
    fromstation = transform(fromstation)
    tostation = transform(tostation)
    searchdate = datetime.datetime.now().strftime("%Y/%m/")
    date = datetime.datetime.now().strftime("%d")
    fromtime = datetime.datetime.now().strftime("%H")+"00"
    searchdate = searchdate+date.zfill(2)
    print(fromtime)
    print(searchdate)
    res = requests.get("http://twtraffic.tra.gov.tw/twrail/mobile/TimeTableSearchResult.aspx?searchdate="+searchdate+"&trainclass=2&fromstation="+fromstation+"&tostation="+tostation+"&fromtime="+fromtime+"&totime=2359")
    res.encoding = "UTF-8"
    soup = BeautifulSoup(res.text, "lxml")
    string = str(soup.select("script")[2].text.split("TRSearchResult.push"))
    string = re.findall(r'[(](.*?)[)]',string)
    if string == "":
        return "今日已無車次"
    string = to_matrix(string,8)
    newstring = [[x[0],x[2],x[3],x[7]] for x in string]
    result = ""
    res = "  車種    出發      抵達     誤點\n--------------------------\n"
    i = 0
    for l in newstring:
        result += " ".join(map(str,l))+"\n"
    result = result.replace("'"," ")
    result = result.replace("車","")
    result = result.replace("快","")
    result = " " + res + result
    print(result)
    return(result)
    
#trainsearch(fromstation, tostation)
c = "回家"
d = "回學校"
trainsearch(c)
#trainsearch(d)
