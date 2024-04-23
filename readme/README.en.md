# web_screenshot_with_highlighted
This project allows users to selectively extract essential information from a webpage by providing only partial parameters, and then save it as an image file.<br>
Btw Especially suitable for websites which presenting data!<br>

example（[original website](https://kmamiz-demo.soselab.tw/insights)）：
![coupling](https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/ac7cab99-9632-428f-96fc-8dffbcd1c866)

## Function
- Capture webpage elements and save them as image files.
- Capture webpage elements, highlight important information, and then save them as image files.

## the Meaning of Noun and Parameter
A webpage can be roughly divided into the following sections: <br>
![all_elements](https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/86ad39c9-2bc8-4be0-8af2-8b16e951b936)


- web element
  - `CHROMEDRIVER_PATH` → path to chromedriver
  - `WAY` → the mode of capture, divided into URL and HTML
  - `URL_or_HTML` → the url/file of web
  - `WINDOW_SIZE` → a dictionary containing:
    - `WIDTH` → the width of the desired window
    - `HEIGHT` → the height of the desired window
  - `CSS_SELECTOR` → CSS selector of the element to be captured
  - `HIDDEN_CSS_SELECTOR` → an array containing all CSS selectors of elements to be hidden (as they might block relevant & important information).
    If no elements need to be hidden, leave the array empty.
  - `WIDTH`, `HEIGHT` → the width and height of the element **（provided by system）** <br>
    ![web_element](https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/d5d53aaf-e53f-4dd7-8b30-1f7962e7f29b)


- relevant information
  - `IMAGES_PATH` → the directory to store the images
  - `IMAGES_PARAM` → a dictionary array allowing customization of parameters for each element
    keys within the dictionary include:
    - `DIRECTION` → whether it's vertical (`vertical`) or horizontal (`horizontal`). Only these two options are available
    - `IMAGE_NAME` → the name of the file to be saved after capturing
    - `TOP_RATIO` → the ratio of cropping from the top
    - `BOTTOM_RATIO` → the ratio of cropping from the bottom
    - `LEFT_RATIO` → the ratio of cropping from the left
    - `RIGHT_RATIO` → the ratio of cropping from the right <br>
  
    [Note] If only capturing is required, IMAGES_PARAM needs to include only `IMAGE_NAME`
    ![ratio](https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/8d8b3aa5-8571-4330-a82b-1e2e93444867)


- important information
  - `IMAGES_PARAM` → a dictionary array allowing customization of parameters for each element (same as mentioned in related information)
    - `SUM` → how many equal parts to divide into
    - `TARGET` → indicates which part (indexed from 0) contains the highlighted important information<br>
    ![important_information](https://github.com/angel08012000/web_screenshot_with_highlighted/assets/58464773/4a05bf2f-755f-4436-9bb1-c1411d8a5b55)

## Parameter Configuration File
Combine the parameters mentioned above into a single JSON file.

path: setting/xxx.json
```json
{
    "CHROMEDRIVER_PATH" : "<<path to chrome driver>>",
    "WAY" : "<<mode of capture, divided into url or html>>",
    "URL_or_HTML" : "<<location of the URL or HTML file>>",
    "WINDOW_SIZE": {
        "WIDTH": "<<desired width of the window>>",
        "HEIGHT": "<<desired height of the window>>"
    },
    "CSS_SELECTOR" : "<<CSS selector of the element to capture>>",
    "HIDDEN_CSS_SELECTOR": ["<<CSS selector of elements to hide>>"],
    "TOGGLE_CSS_SELECTOR": ["<<CSS selector of elements to toggle>>"],
    "IMAGES_PATH" : "<<prefix path to store photos>>",
    "IMAGES_PARAM" : [
        {
            "DIRECTION": "<<direction to use, vertical or horizontal>>",
            "IMAGE_NAME": "<<name of the photo to be saved>>",
            "TOP_RATIO" : "<<top cropping ratio>>", 
            "BOTTOM_RATIO" : "<<bottom cropping ratio>>", 
            "LEFT_RATIO" : "<<left cropping ratio>>", 
            "RIGHT_RATIO" : "<<right cropping ratio>>",
            "SUM" : "<<total number of parts to divide into>>",
            "TARGET" : "<<index of the part containing the highlighted information, starting from 0>>"
        },
    ]
}
```

## Workflow
1. Read parameters from the parameter file.
2. Determine whether to open the webpage using a URL or HTML.
3. Use the webdriver to open the webpage.
4. Use the webdriver to locate the webpage element to be highlighted.
5. Check if the "number of elements to be captured" matches the "number of parameters provided by the user". If they do not match, print an error message and return.
6. Attempt to hide or toggle specified elements. If unsuccessful, print an error message and terminate.
7. Capture and highlight important information according to the parameters provided by the user, then save it as an image file.

## Customizable Adjustments
In step 6 of the algorithm, we provide a custom_function(self, driver, param).
Within this function, you are free to adjust according to your specific requirements!

We also provide two additional functions:
- `find_and_hide_elements(self, driver, param)` → locate and hide specified elements
- `find_and_toggle_element(self, driver, param)` → locate and toggle specified elements

## Project Structure
- env `your environment`
- requirements.txt
- html `if the capture mode is HTML, place the files in this folder`
- settings `place the parameter configuration file in this folder`
- images `if you want to store the images in this folder, set "IMAGES_PATH" : "./images"`
- chromedriver `if not available, please download the corresponding chromedriver`
- main.py
- user.py `customize your program here`

## Usage
Clone the Project:
```
git clone https://github.com/angel08012000/web_screenshot_with_highlighted.git
```

Go to the Project Location
```
cd <<the location of project>>
```

Setting up the Environment
```
pip3 install virtualenv #install if not already installed
virtualenv <<environment_name>> #create the environment
source <<environment_name>>/bin/activate #activate the environment
```

Downloading Required Packages:
```
pip install -r requirements.txt
```

Customize Your Program
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

#highlighted.screenshot_with_highlighted(file name, highlighted or not)
c = CustomHighlighted("KMamiz", True)
c.screenshot_with_highlighted()
```
