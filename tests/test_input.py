import pytest

from core.input_helper import InputHelper
from playwright.sync_api import expect

@pytest.mark.smoke
@pytest.mark.parametrize("input_text", [
    "Test_123",
    "Test_1234",
    "Test_12345",
    "Test_123456",
                                        ])
def test_input_field(page, input_text):
    input_page = InputHelper(page)
    input_page.open("https://www.qa-practice.com/elements/input/simple")
    input_page.click_by_Text_input()
    input_page.fill_and_submit(input_text)
    result = input_page.page.locator("#result-text")
    expect(result).to_have_text(input_text)
