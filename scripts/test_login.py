import os
import sys

import time

sys.path.append(os.getcwd())

import allure

from base.read_yaml import ReadYaml

import pytest

from page.page_in import PageIn


def get_data():
    arrs = []
    for data in ReadYaml("login_data.yaml").read_yaml().values():
        arrs.append((data.get("username"), data.get("password"), data.get("expect_result"), data.get("expect_toast")))
    return arrs


# 建类
class Testlogin():
    def setup_class(self):
        self.login = PageIn().page_get_pagelogin()
        self.login.page_click_me()
        self.login.page_click_username_link()

    def teardown_class(self):
        time.sleep(5)
        self.login.driver.quit()

    @pytest.mark.parametrize("username,password,expect_result,expect_toast", get_data())
    @allure.step("开始执行登录测试")
    def test_login(self, username, password, expect_result, expect_toast):
        login = self.login
        if expect_result:
            try:
                # 输入用户名
                login.page_input_username(username)
                # 输入密码
                login.page_input_password(password)
                # 点击登录
                login.page_click_btn()
                # 断言
                assert expect_result in login.page_get_nickname()
                # 点击设置
                login.page_click_setting()
                # 点击退出,确认退出
                login.page_click_logout()
                # 点击我
                login.page_click_me()
                # 点击已有账号 去登录
                login.page_click_username_link()
            except AssertionError:
                    # 失败截图
                    login.base_get_image()
                    # 截图写入报告
                    with open("./image/faild.png", "rb") as f:
                        allure.attach("失败原因", f.read(), allure.attach_type.PNG)
        else:
            try:
                # 输入用户名
                login.page_input_username(username)
                # 输入用户名
                login.page_input_password(password)
                # 点击登录
                login.page_click_btn()
                # 断言
                assert expect_toast in login.base_get_toast(expect_toast)
            except AssertionError:
                # 截图
                login.base_get_image()
                # 截图写入报告
                with open("./image/faild.png", "rb") as f:
                    allure.attach("失败原因", f.read(), allure.attach_type.PNG)


