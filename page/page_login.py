import allure

import page
from base.base import Base


# 创建类
class PageLogin(Base):
    # 点击我
    @allure.step("点击我")
    def page_click_me(self):
        self.base_click(page.login_click_me)

    # 点击已有账号,登录
    @allure.step("点击已有账号,登录")
    def page_click_username_link(self):
        self.base_click(page.login_click_username_link)

    # 输入用户名
    @allure.step("输入用户名")
    def page_input_username(self, username):
        self.base_input(page.login_input_username, username)

    # 输入密码
    @allure.step("输入用密码")
    def page_input_password(self,password):
        self.base_input(page.login_input_password, password)

    # 点击登录
    @allure.step("点击登录")
    def page_click_btn(self):
        self.base_click(page.login_click_btn)

    # 获取昵称
    @allure.step("获取昵称")
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    # 获取toast
    @allure.step("获取toast")
    def page_get_toast(self, msg):
        return self.base_get_toast(msg)

    # 点击设置
    @allure.step("点击设置")
    def page_click_setting(self):
        self.base_click(page.login_click_setting)

    # 拖拽
    @allure.step("拖拽  从消息推送 拖拽 到修改密码")
    def page_drag_and_drop(self):
        # 定位消息推送
        el1 = self.base_find_element(page.login_setting_notification)
        # 定位修改密码
        el2 = self.base_find_element(page.login_setting_modify_pwd)
        self.base_drag_and_drop(el1, el2)

    # 点击退出
    @allure.step("点击退出")
    def page_click_logout_btn(self):
        self.base_click(page.login_setting_logout)

    # 确定退出
    @allure.step("确认退出")
    def page_click_logout_ok(self):
        self.base_click(page.login_ymdialog_right_button)

    # 整体封装 退出
    def page_click_logout(self):
        # 拖拽
        self.page_drag_and_drop()
        # 点击退出
        self.page_click_logout_btn()
        # 确认退出
        self.page_click_logout_ok()



