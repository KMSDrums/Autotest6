from playwright.sync_api import sync_playwright
import data

with sync_playwright() as p:
    for browser_type in [p.chromium]:
        email = data.email()
        password = data.password()
        print(browser_type.name, 'start test')
        browser = browser_type.launch(headless=False)
        page = browser.new_page(locale='en-GB')
        page.goto("http://int.dev.clusters.cyber.bet")
        page.click("text=Log in")
        page.type("input[name='email']", email)
        page.type("input[name='password']", password)
        page.click("text=Log in")
        page.click("text=deposit")
        page.click("text=mastercard")
        page.wait_for_timeout(2000)
        page.click("text=pay 20 EUR")
        page.wait_for_timeout(10000)
        page.type("input[name='PaymentData[pan]']", '40000000000000002')
        page.type("input[name='PaymentData[card_holder]']", 'Ivan Ivanov')
        page.click("[id=month-1]")
        page.wait_for_timeout(1000)
        page.click("[month-1 > option:nth-child(3)]")
        page.type("input[name='PaymentData[year]']", '2023')
        page.type("input[name='PaymentData[cvv]']", '123')
        page.wait_for_timeout(5000)
        browser.close()
        print('end of test')

    print('End of All Tests!')