from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# 创建类
class Base():
    # 初始化driver
    def __init__(self, driver):
        self.driver = driver

    # 查找
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 输入
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 点击
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 获取昵称
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 截图
    def base_get_image(self):
        self.driver.get_screenshot_as_file("./image/faild.png")

    # 拖拽
    def base_drag_and_drop(self, el1, el2):
        self.driver.drag_and_drop(el1, el2)

    # 获取toast
    def base_get_toast(self, msg):
        loc = By.XPATH, "//*[contains(@text,'"+msg+"')]"
        return self.base_find_element(loc).text
