import allure
from allure_commons.types import Severity
from mriya_tests.web.check_shop_on_the_map import CheckShop

check_shop = CheckShop()


@allure.parent_suite('Web')
@allure.label('owner', 'ischenkoalex')
@allure.tag('Mriya Resort')
@allure.title('Check Shop On The Map')
@allure.severity(Severity.MINOR)
def test_check_on_the_shop():
    check_shop.open()
    check_shop.accept_cookies()
    check_shop.scroll_to_button_legend()
    check_shop.choose_filter_shops()
    check_shop.accept_choose()
    check_shop.check_our_shop()