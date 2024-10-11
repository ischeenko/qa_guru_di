import allure
from allure_commons.types import Severity
from mriya_tests.web.check_email_and_telegram import CheckEmailAndTelegram

check_email_telegram = CheckEmailAndTelegram()


@allure.parent_suite('Web')
@allure.label('owner', 'ischenkoalex')
@allure.tag('Mriya Resort')
@allure.title('Check Shop On The Map')
@allure.severity(Severity.MINOR)
def test_check_email_telegram():
    check_email_telegram.open()
    check_email_telegram.accept_cookies()
    check_email_telegram.hover_contacts()
    check_email_telegram.check_telegram()
    check_email_telegram.check_email()