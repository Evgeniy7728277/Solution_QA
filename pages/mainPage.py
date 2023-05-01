"""Go to the default page Manager Layer/First Enter"""

from selenium.webdriver.common.by import By

class QpcInternalURL:
    Search_Input = (By.NAME,"baseUrlApi")
    Search_Button = (By.CSS_SELECTOR, "[class='MuiBox-root css-1jmd00u']")

    def __init__(self, browser):
        self.browser = browser

    def enter_url(self, url):
        self.browser.find_element(*self.Search_Input).send_keys(url)

        #self.browser.implicitly_wait(2)
    def press_button_save(self):
        self.browser.find_element(*self.Search_Button).click()

    pass
