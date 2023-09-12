# web_screenshot_with_highlighted
該專案讓使用者僅需提供部分參數，即可圈選（optional）某個網頁上的重要資訊，並將之存為 PNG 圖檔。<br>
Btw 特別適合用於呈現數據之網站！<br>

範例如下（[原始網站](https://kmamiz-demo.soselab.tw/insights)）：
![coupling](https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/ac7cab99-9632-428f-96fc-8dffbcd1c866)

## 功能
- 截圖網頁元素，並將之存為 PNG 圖檔
- 截圖網頁元素，並圈選重要資訊，再將之存為 PNG 圖檔

## 名詞、參數解釋
一個網頁可以大致分為以下區塊：<br>
<img width="518" alt="截圖 2023-07-18 上午12 09 42 (1)" src="https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/9c5c8427-23b2-4964-ba10-81f179362d2c">

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
  - `WIDTH`, `HEIGHT` → 該元素之寬、高 **（由系統提供）**
    <img width="518" alt="截圖 2023-07-18 上午12 59 36" src="https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/32b329b3-cf9f-4cbf-a4de-d5d5a15163fc">

- 相關資訊
  - `IMAGES_PATH` → 儲存的圖檔要放在哪
  - `IMAGES_PARAM` → 是一個字典陣列，可為每個元素客製化相關參數
    字典內的 Key 包含了
    - `DIRECTION` → 代表是直式（`vertical`）還是橫式（`horizontal`），只有這兩個可以選擇   
    - `IMAGE_NAME` → 截圖完後，要存的檔案名稱
    - `TOP_RATIO` → 上方需裁切之比例
    - `BOTTOM_RATIO` → 下方需裁切之比例
    - `LEFT_RATIO` → 左邊需裁切之比例
    - `RIGHT_RATIO` → 右邊需裁切之比例
    <img width="518" alt="截圖 2023-07-18 上午12 57 17" src="https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/c830695b-0f27-49a0-b03b-c33e7c478b3a">

- 重要資訊
  - `IMAGES_PARAM` → 是一個字典陣列，可為每個元素客製化相關參數（跟相關資訊中的是同一個）
    - `SUM` → 要平均分成幾份
    - `TARGET` → 圈起來的重要資訊是在第幾份（從0開始）<br>
    <img width="529" alt="截圖 2023-07-18 上午12 58 12" src="https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/9d3d2124-8ccc-4d6e-8bf3-b1c9f796965e">

## 參數設定檔

## 可客製化調整部份
