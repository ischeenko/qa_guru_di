import allure
from selene import browser, be, have, command

class CheckBenefit:

    def open(self):
        with allure.step('Открываем главную страницу'):
            browser.open('/')

    def accept_cookies(self):
        with allure.step('Подтверждаем cookies'):
            browser.element('.popup--content .button_wrapper .button').click()

    def click_button(self):
        with allure.step('Кликаем на кнопку Виллы'):
            browser.element('.button-dark[title="Виллы"]').click()

    def choose_apartament(self):
        with allure.step('Выбираем апартаменты'):
            browser.element('.card[title="Президентские виллы"]').perform(
                command.js.scroll_into_view).click()

    def look_all_amenities(self):
        with allure.step('Кликаем кнопку "Увидеть все"'):
            browser.element(
                '.button[data-openpopup="popup_residence_object_amenities'
                '"]').perform(
                command.js.scroll_into_view).click()

    def check_our_benefit(self):
        with allure.step('Проверяем, есть ли в апартаментах Джакузи'):
            browser.element('.amenity--icon[title="Джакузи"]').should(
                be.visible)