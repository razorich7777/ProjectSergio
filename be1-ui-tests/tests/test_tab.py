from playwright.sync_api import Page, BrowserContext, expect

def test_tabs(page: Page, context: BrowserContext):
    page.goto("https://nomadlist.com/")
    with context.expect_page() as new_tab_event:
        page.get_by_alt_text('Get insured').click()
        new_tab = new_tab_event.value

    text = 'Welcome to SafetyWing'
    new_tab.get_by_text('Sign me up').click()
    (expect(new_tab.get_by_text('Welcome to SafetyWing'))
     .to_have_text(text))