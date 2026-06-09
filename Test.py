def dailog_accept(dailog):
    dailog.accept()

def dismisss_dailog(dailog):
    dailog.dismiss()

def prompt_dailog(dailog):
    dailog.accept("omkarataniure")


page.once("dailog", dailog_accept())



from playwright.sync_api import sync_playwright

def handle_dailg(dialog):
  print(dialog.massage)
  dialog.accept()


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False, channel="chromeS")


    page=browser.new_page()
    page.goto("https://demoqa.com/automation-practice-form")


    page.locator("#firstName").type("omkaratanure")

    page.locator("#lastName").fill("atanure")
    page.get_by_placeholder("name@example.com").fill("omkaratanure111@gmail.com")

    page.locator("input[value='Male']").check()

    page.locator("#userNumber").type("99869856")
    page.locator("#dateOfBirthInput").click()


    page.locator(".react-datepicker__year-select").select_option("1902")
    page.wait_for_timeout(30000)
    page.locator(".react-datepicker__month-select").select_option("9")
    page.wait_for_timeout(30000)

    page.locator("[aria-label='Choose Wednesday, June 3rd, 2026']").click()

    page.locator("#hobbies-checkbox-1").check()

    page.locator("#uploadPicture").set_input_files("omkar.pdf")

    page.get_by_text("Alerts, Frame & Windows").click()

    page.get_by_text("Alerts").click()
    page.locator("#alertButton").click()

    page.on("dialog",handle_dailg)



    page.locator(".css-hlgwow").fill("Rajasthan")

    page.locator(".css-19bb58m").fill("Jaipur")
    page.screenshot(path="demoscreeshot.png", full_page=True)







