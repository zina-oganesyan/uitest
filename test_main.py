from playwright.sync_api import expect

#2. Задача Playwright:
#Условие: Написать тест, который открывает веб-страницу https://playwright.dev/
# и проверяет что заголовок страницы соответствует ожидаемому значению.
# Тест необходимо запустить минимум на 2 разных браузерах.
#Ожидаемый результат: Тест успешно проходящий проверку заголовка.

# Проверка заголовка страницы выполнена успешно.
def test_1(browser_name, playwright):
    browser = getattr(playwright, browser_name).launch()
    page = browser.new_page()
    page.goto('https://playwright.dev')
    title = page.locator("h1.hero__title")
    expect(title).to_have_text("Playwright enables reliable end-to-end testing for modern web apps.")
    browser.close()

# Проверка названия страницы выполнена успешно.
def test_2(browser_name, playwright):
    browser = getattr(playwright, browser_name).launch()
    page = browser.new_page()
    page.goto('https://playwright.dev')
    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
    browser.close()