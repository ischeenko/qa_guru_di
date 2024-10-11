import allure
from selene import browser, have, be, command


class CheckTransfer:

    def open(self):
        with allure.step('Открываем главную страницу'):
            browser.open('/')

    def accept_cookies(self):
        with allure.step('Подтверждаем cookies'):
            browser.element('.popup--content .button_wrapper .button').click()

    def click_button(self):
        with allure.step('Кликаем кнопку "Как добраться"'):
            browser.element('.button-dark[title="Как добраться"]').click()

    def choose_card_with_car(self):
        with allure.step('Выбираем карту с машиной'):
            browser.element('.card[data-popup_cascade="721"').perform(
                command.js.scroll_into_view).click()

    def type_name(self, value):
        with allure.step('Заполняем имя'):
            browser.element('[type="text"]').perform(
                command.js.scroll_into_view).type(value)

    def type_phone_number(self, value):
        with allure.step('Заполняем телефон'):
            browser.element('[type="tel"]').type(value)

    def check_button_without_checkbox(self):
        with allure.step('Проверяем, что кнопка неактивна без чек-боксов'):
            browser.element('.button-accent').should(be.enabled)