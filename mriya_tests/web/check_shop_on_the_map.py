import allure
from selene import browser, be, have, command


class CheckShop:
    def open(self):
        with allure.step('Открываем главную страницу'):
            browser.open('/')

    def accept_cookies(self):
        with allure.step('Подтверждаем cookies'):
            browser.element('.popup--content .button_wrapper .button').click()

    def scroll_to_button_legend(self):
        with allure.step('Скроллим до кнопки Легенды'):
            browser.element('.scheme_legend--title').perform(
                command.js.scroll_into_view).click()

    def choose_filter_shops(self):
        with allure.step('Выбираем в фильтрах магазины'):
            browser.element('.scheme_legend--filter[data-type="shops"]').click()

    def accept_choose(self):
        with allure.step('Кликаем кнопку для подтверждения'):
            browser.element('.scheme_legend--title').click()

    def check_our_shop(self):
        with allure.step('Проверяем магазин на карте'):
            browser.element('.placemark-shop[data-popup_cascade="66"]').should(
                be.visible)