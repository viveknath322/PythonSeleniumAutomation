class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.username = "//input[@id='txtUsername']"
        self.password = "//input[@id='txtPassword']"
        self.loginbutton = "//input[@id='btnLogin']"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.loginbutton).click()

