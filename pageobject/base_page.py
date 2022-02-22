class BasePage:

    def __init__(self, driver, url, title):
        self.driver = driver
        self.url = url
        self.title = title
