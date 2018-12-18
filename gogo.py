import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import re
import sqlite3

def transform2(station):
    if station == "台北" or station == "臺北": 
        return "977abb69-413a-4ccf-a109-0272c24fd490"
    elif station == "南港" :
        return "2f940836-cedc-41ef-8e28-c2336ac8fe68"
    elif station == "板橋" :
        return "e6e26e66-7dc1-458f-b2f3-71ce65fdc95f"
    elif station == "桃園" :
        return "fbd828d8-b1da-4b06-a3bd-680cdca4d2cd"
    elif station == "新竹" :
        return "a7a04c89-900b-4798-95a3-c01c455622f4"
    elif station == "苗栗" :
        return "e8fc2123-2aaf-46ff-ad79-51d4002a1ef3"
    elif station == "台中" or station == "臺中" :
        return "3301e395-46b8-47aa-aa37-139e15708779"
    elif station == "彰化" :
        return "38b8c40b-aef0-4d66-b257-da96ec51620e"
    elif station == "雲林" :
        return "5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f"
    elif station == "台南" or station == "臺南":
        return "9c5ac6ca-ec89-48f8-aab0-41b738cb1814"
    elif station == "嘉義" :
        return "60831846-f0e4-47f6-9b5b-46323ebdcef"
    elif station == "左營" :
        return "f2519629-5973-4d08-913b-479cce78a356"
    else:
        return "0"

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
    if b[2] == "火車":
        if transform(b[0]) == 0:
            return False
        if transform(b[1]) == 0:
            return False
    elif b[2] == "高鐵":
        if transform2(b[0]) == 0:
            return False
        if transform2(b[1]) == 0:
            return False
    else:
       return False
    conn = sqlite3.connect('user')
    c = conn.cursor()
    c.execute('REPLACE INTO setting VALUES(?,?,?,?)',(1,b[0],b[1],b[2]))
    conn.commit()
    return True

#a = "台南\n台北\n火車"
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
#trainsearch(d)
def thsrcsearch(a):
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
    fromstation = transform2(fromstation)
    tostation = transform2(tostation)
    searchdate = datetime.datetime.now().strftime("%Y/%m/")
    date = datetime.datetime.now().strftime("%d")
    fromtime = datetime.datetime.now().strftime("%H")+":00"
    searchdate = searchdate+date.zfill(2)
    url = 'http://m.thsrc.com.tw/tw/TimeTable/SearchResult'
    form_data = {
        'startStation':fromstation,
        'endStation':tostation,
        'theDay':searchdate,
        'timeSelect':fromtime,
        'waySelect':'DepartureInMandarin'
    }
    response_post = requests.post(url,data = form_data)
    soup = BeautifulSoup(response_post.text, 'lxml')
    soup = soup.find('div','timeResultList ui-grid-b')
    string = str(soup.findAll('a'))
    string = re.sub(u"\\<.*?\\>","",string)
    string = re.sub(u"\\(.*?\\)","",string)
    string = ' '.join(string.split())
    string = string.split(',')
    string = to_matrix(string,3)
    result = ""
    res = "  車次  出發-抵達   自由車廂數\n--------------------------\n"
    for l in string:
        result += " ".join(map(str,l))+"\n"
    result = result.replace(" ( "," (")
    result = result.replace(" - ","-")
    result = result.replace(" ) ",")")
    result = result.replace("[","")
    result = result.replace("]","")
    result = res + result
    print(result)
    return(result)
#trainsearch(c)
#thsrcsearch(c)
def search(a):
    conn = sqlite3.connect('user')
    c = conn.cursor()
    c.execute('SELECT * FROM setting')
    d = c.fetchone()
    if d[3] == "火車":
        return trainsearch(a)
    elif d[3] == "高鐵":
        return thsrcsearch(a)

