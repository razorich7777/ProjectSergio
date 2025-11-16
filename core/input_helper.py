from playwright.sync_api import Page

from .base_helper import BaseHelper

class InputHelper(BaseHelper):
    input_locator = "#id_text_string"
    result_locator = "#result-text"
    text_input_tab = "Text input"

    def __init__(self, page: Page):
        super().__init__(page)

    def fill_and_submit(self, text: str):
        self.page.fill(self.input_locator, text)
        self.page.press(self.input_locator, "Enter")

    def get_result_text(self) -> str:
        return self.page.text_content(self.result_locator)

    def click_by_Text_input(self):
        self.page.get_by_text(self.text_input_tab)