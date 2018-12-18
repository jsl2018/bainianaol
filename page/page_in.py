import allure

from base.get_driver import get_driver
from page.page_login import PageLogin

# 获取driver
driver = get_driver()


# 建类
class PageIn():
    # 获取登录页面对象
    @allure.step("实例化登录页面")
    def page_get_pagelogin(self):
        return PageLogin(driver)
