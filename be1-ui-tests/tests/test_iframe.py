from playwright.sync_api import Page
from com.core.BaseHelper import BaseHelper
from tests import TestBase

class TestIframe(TestBase):

    def test_iframe(self, page: Page):
        page.goto_home_page(page)
        base = BaseHelper()
        base.click_by_navbar_iframe(page)



