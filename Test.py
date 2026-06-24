from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=100)

    page=browser.new_page(no_viewport=True)


    page.goto(
    "https://www.hyrtutorials.com/p/window-handles-practice.html"
    )

    with page.expect_popup() as newpage:
        page.get_by_text("Open New Window").click()


    new_page=newpage.value

    page.wait_for_load_state()

    selected_option=new_page.locator("#selectnav1").select_option("Tech News")

    print(selected_option)

    page.wait_for_timeout(30000)