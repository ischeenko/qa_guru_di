import allure
from selene import browser, be, have, command


class CheckName:

    def open(self):
        with allure.step('Открываем главную страницу'):
            browser.open('/')

    def accept_cookies(self):
        with allure.step('Подтверждаем cookies'):
            browser.element('.popup--content .button_wrapper .button').click()

    def open_menu(self):
        with allure.step('Открываем меню'):
            browser.element('.menu_button').click()

    def click_button(self):
        with allure.step('Кликаем кнопку "Оздоровление"'):
            browser.element('.menu--item[title="Оздоровление"]').click()

    def swipe_carousel(self):
        with allure.step('Свайпаем карусель до нужного блока'):
            browser.element('.swiper-button-next').click()

    def click_card(self):
        with allure.step('Кликаем на нужный блок'):
            browser.element('.card[title="Косметология"]').click()

    def check_text_block(self):
        with allure.step('Проверяем название блока'):
            browser.element('.block--head_title').should(have.text(
                "КОСМЕТОЛОГИЧЕСКИЕ\nУСЛУГИ"))