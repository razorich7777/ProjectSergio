from playwright.sync_api import Page

class BaseHelper:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def click(self):
        self.page.click()