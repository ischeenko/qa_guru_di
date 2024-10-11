import allure
from allure_commons.types import Severity
from mriya_tests.web.check_benefit import CheckBenefit

check_benefit = CheckBenefit()


@allure.parent_suite('Web')
@allure.label('owner', 'ischenkoalex')
@allure.tag('Mriya Resort')
@allure.title('Check Benefit on the Apartmament')
@allure.severity(Severity.MINOR)
def test_check_benefit():
    check_benefit.open()
    check_benefit.accept_cookies()
    check_benefit.click_button()
    check_benefit.choose_apartament()
    check_benefit.look_all_amenities()
    check_benefit.check_our_benefit()
