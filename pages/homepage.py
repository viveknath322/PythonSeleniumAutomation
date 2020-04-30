class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.welcome = "//a[@id='welcome']"
        self.logout = "//a[contains(text(),'Logout')]"

    def click_welcome(self):
        self.driver.find_element_by_xpath(self.welcome).click()

    def clicl_logout(self):
        self.driver.find_element_by_xpath(self.logout).click()