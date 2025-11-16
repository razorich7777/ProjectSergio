import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def context(pytestconfig):
    browser_option = pytestconfig.getoption("--browser")
    # Если вернулся список, берём первый элемент
    browser_name = browser_option[0] if isinstance(browser_option, list) else browser_option

    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(channel="chrome", headless=False)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=False)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=False)
        else:
            raise ValueError(f"Unknown browser: {browser_name}")

        context = browser.new_context()
        yield context
        context.close()
        browser.close()
