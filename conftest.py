import pytest
from playwright.sync_api import sync_playwright
import allure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Событие после выполнения каждого теста
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        # Если тест упал, делаем скриншот и прикладываем его к отчету
        page = item.funcargs.get("page", None)
        if page:
            screenshot = page.screenshot()
            allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
