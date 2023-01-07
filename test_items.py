from selenium.webdriver.common.by import By
import time

def test_add_to_basket_button(browser):
    browser.implicitly_wait(3)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    basket_button = browser.find_elements(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    assert len(basket_button)>0, "Кнопка добавления в корзину не найдена"