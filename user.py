import main as m

class CustomHighlighted(m.Highlighted):
    def __init__(self, file_name, highlighted):
        self.file_name = file_name
        self.highlighted = highlighted
    
    def custom_function(self, driver, param):
        # you can custom code here
        self.find_and_hide_elements(driver, param)

c = CustomHighlighted("KMamiz_schema", False)
# c = CustomHighlighted("KMamiz_html", True)
# c = CustomHighlighted("Grade_html", True)
# c = CustomHighlighted("TradingEconomics", True)
# c = CustomHighlighted("Twse", True)
c.screenshot_with_highlighted()