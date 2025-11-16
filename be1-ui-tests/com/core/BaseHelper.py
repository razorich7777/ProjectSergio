class BaseHelper:
    def click_by_navbar_iframe(self, page):
        page.frame_locator('iframe').locator('.navbar-toggler-icon').click()

