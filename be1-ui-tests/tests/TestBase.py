import pytest
from playwright.sync_api import Page

@pytest.fixture
def goto_home_page(page: Page):
    page.goto("https://www.qa-practice.com/elements/iframe/iframe_page")