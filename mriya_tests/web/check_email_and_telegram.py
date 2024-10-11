import allure
from selene import browser, be, have, command


class CheckEmailAndTelegram:

    def open(self):
        with allure.step('Открываем главную страницу'):
            browser.open('/')

    def accept_cookies(self):
        with allure.step('Подтверждаем cookies'):
            browser.element('.popup--content .button_wrapper .button').click()

    def hover_contacts(self):
        with allure.step('Наводим курсор на номер телефона и контакты'):
            browser.element('.header--contacts').hover()

    def check_telegram(self):
        with allure.step('Проверяем, есть ли Телеграмм'):
            browser.element('[title="Telegram"]').should(be.visible)

    def check_email(self):
        with allure.step('Проверяем, есть ли почта'):
            browser.element('[title="info@mriyaresort.com"]').should(be.visible)