# web_screenshot_with_highlighted
該專案讓使用者僅需提供部分參數，即可圈選（optional）某個網頁上的重要資訊，並將之存為圖檔。<br>
Btw 特別適合用於呈現數據之網站！<br>

範例如下（[原始網站](https://kmamiz-demo.soselab.tw/insights)）：
![coupling](https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/ac7cab99-9632-428f-96fc-8dffbcd1c866)

## 功能
- 截圖網頁元素，並將之存為圖檔
- 截圖網頁元素，並圈選重要資訊，再將之存為圖檔

## 名詞、參數解釋
一個網頁可以大致分為以下區塊：<br>
![all_elements](https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/86ad39c9-2bc8-4be0-8af2-8b16e951b936)


- 網頁元素
  - `CHROMEDRIVER_PATH` → chromedriver 的路徑
  - `WAY` → 要抓取的模式，分為 url、html
  - `URL_or_HTML` → 該網頁的連結
  - `WINDOW_SIZE` → 是一個字典
    字典內的 Key 包含了
    - `WIDTH` → 代表欲開啟視窗之寬
    - `HEIGHT` → 代表欲開啟視窗之高
  - `CSS_SELECTOR` → 欲抓取元素的 css selector
  - `HIDDEN_CSS_SELECTOR` → 是一個陣列，欲隱藏元素之所有 css selector（因為有可能擋到相關＆重要資訊）
    若沒有需要隱藏之元素，就放空陣列即可
  - `WIDTH`, `HEIGHT` → 該元素之寬、高 **（由系統提供）** <br>
    ![web_element](https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/d5d53aaf-e53f-4dd7-8b30-1f7962e7f29b)


- 相關資訊
  - `IMAGES_PATH` → 儲存的圖檔要放在哪
  - `IMAGES_PARAM` → 是一個字典陣列，可為每個元素客製化相關參數
    字典內的 Key 包含了
    - `DIRECTION` → 代表是直式（`vertical`）還是橫式（`horizontal`），只有這兩個可以選擇   
    - `IMAGE_NAME` → 截圖完後，要存的檔案名稱
    - `TOP_RATIO` → 上方需裁切之比例
    - `BOTTOM_RATIO` → 下方需裁切之比例
    - `LEFT_RATIO` → 左邊需裁切之比例
    - `RIGHT_RATIO` → 右邊需裁切之比例 <br>
  
    [註] 若單純截圖，則 IMAGES_PARAM 僅需包含 `IMAGE_NAME`
    ![ratio](https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/8d8b3aa5-8571-4330-a82b-1e2e93444867)


- 重要資訊
  - `IMAGES_PARAM` → 是一個字典陣列，可為每個元素客製化相關參數（跟相關資訊中的是同一個）
    - `SUM` → 要平均分成幾份
    - `TARGET` → 圈起來的重要資訊是在第幾份（從0開始）<br>
    ![important_information](https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/4a05bf2f-755f-4436-9bb1-c1411d8a5b55)


## 參數設定檔
將上述所提及之參數合併為一個 json 檔案

path: setting/xxx.json
```json
{
    "CHROMEDRIVER_PATH" : "<<chrome driver 的路徑>>",
    "WAY" : "<<要抓取的模式，分為 url、html>>",
    "URL_or_HTML" : "<<放 url 或者 html 的檔案位置>>",
    "WINDOW_SIZE": {
        "WIDTH": "<<欲開啟視窗的寬>>",
        "HEIGHT": "<<欲開啟視窗的高>>"
    },
    "CSS_SELECTOR" : "<<要抓取元素的 css selector>>",
    "HIDDEN_CSS_SELECTOR": ["<<要隱藏元素的 css selector>>"],
    "TOGGLE_CSS_SELECTOR": ["<<要 toggle 元素的 css selector>>"],
    "IMAGES_PATH" : "<<要存放照片的前綴路徑>>",
    "IMAGES_PARAM" : [
        {
            "DIRECTION": "<<要使用的方向，分為直式（vertical）、橫式（horizontal）>>",
            "IMAGE_NAME": "<<要存的照片名稱>>",
            "TOP_RATIO" : "<<上方裁切比例>>", 
            "BOTTOM_RATIO" : "<<下方裁切比例>>", 
            "LEFT_RATIO" : "<<左側裁切比例>>", 
            "RIGHT_RATIO" : "<<右側裁切比例>>",
            "SUM" : "<<總共要平分成幾份>>",
            "TARGET" : "<<要圈選的是在第幾份，從 0 開始>>"
        },
    ]
}
```

## 演算法
1. 讀取參數檔的參數
2. 判斷是用 url 還是 html 開啟網頁
3. 利用 webdriver 開啟網頁
4. 利用 webdriver 找定欲圈選之網頁元素
5. 檢查`「欲抓取之元素數量」`＆`「使用者提供參數數量」` 是否相符
   若不符，則印出錯誤訊息並 return
6. 試著隱藏、切換指定元素
   若失敗，則印出錯誤訊息並結束
7. 利用「使用者提供之參數」截圖＆圈選重要資訊，並存成圖檔

## 可客製化調整部份
在演算法的步驟6中，我們提供了一個 `custom_function(self, driver, param)`
在這個 function 裡，你可以根據你的情況自由調整！

我們也提供了另外兩個 function
- `find_and_hide_elements(self, driver, param)` → 尋找並隱藏指定元素
- `find_and_toggle_element(self, driver, param)` → 尋找並切換指定元素

## 使用方式
``` python
# user.py
import main as m

class CustomHighlighted(m.Highlighted):
    def __init__(self, file_name, highlighted):
        self.file_name = file_name
        self.highlighted = highlighted
    
    def custom_function(self, driver, param):
        # you can custom code here
        self.find_and_hide_elements(driver, param)

#highlighted.screenshot_with_highlighted(檔案名稱, 是否要 highlighted)
c = CustomHighlighted("KMamiz", True)
c.screenshot_with_highlighted()
```
