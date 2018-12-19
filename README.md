# TOC-Project
## 說明
此chatbot的設計是為了個人所需，也針對頻繁往返兩地的學子，臨時起意要回家，或被迫趕緊趕回學校，此chatbot方便您**快速查詢往返兩地的即時車次**（包含即時車況如誤點），省去總得上網重新輸入出發抵達日期時間而進行搜尋的繁瑣步驟～

## 如何操作
開啟聊天室，輸入任何字，會出現button顯示三個選項
* **設定：** 初次使用請先設定，並依照提示依序輸入
* **回家：** 根據您的輸入，回傳回家的即時車次
* **回學校：** 根據您的輸入，回傳回學校的即時車次

![show-fsm](https://github.com/emschenn/TOC-Project/blob/master/fsm.png)

## 使用技術
* **高鐵車次**
   以POST方法向網站發送資料Request，再以BeautifulSoup取得網頁內容，進行字串處理
* **臺鐵車次**
   重組網址，以GET取得以javascript動態更新的網頁，再以BeautifulSoup取得網頁內容，進行字串處理
* **資料設定**
   使用sqlite3資料庫，儲存使用者輸入的資料，因為是方便兩地的搜尋，故只設定一筆資料，更改則會replace
* **Deploy using heroku**

## ChatBot DEMO
此 DEMO 顯示**start** -> 設定為火車往返台南高雄兩地之結果 -> 設定為高鐵往返台南左營兩地之結果 
![demo](https://github.com/emschenn/TOC-Project/blob/master/demo.jpg)

