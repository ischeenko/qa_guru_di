import allure
from allure_commons.types import Severity
from mriya_tests.web.check_transfer_without_checkbox import CheckTransfer

check_transfer = CheckTransfer()


@allure.parent_suite('Web')
@allure.label('owner', 'ischenkoalex')
@allure.tag('Mriya Resort')
@allure.title('Check Transfer')
@allure.severity(Severity.MINOR)
def test_check_transfer():
    check_transfer.open()
    check_transfer.accept_cookies()
    check_transfer.click_button()
    check_transfer.choose_card_with_car()
    check_transfer.type_name('Test')
    check_transfer.type_phone_number('71231231212')
    check_transfer.check_button_without_checkbox()