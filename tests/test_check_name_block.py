import allure
from allure_commons.types import Severity
from mriya_tests.web.check_name_block import CheckName

check_block = CheckName()


@allure.parent_suite('Web')
@allure.label('owner', 'ischenkoalex')
@allure.tag('Mriya Resort')
@allure.title('Check Shop On The Map')
@allure.severity(Severity.MINOR)
def test_check_name_block():
    check_block.open()
    check_block.accept_cookies()
    check_block.open_menu()
    check_block.click_button()
    check_block.swipe_carousel()
    check_block.click_card()
    check_block.check_text_block()