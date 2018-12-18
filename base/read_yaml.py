import os

import pytest
import yaml


class ReadYaml():
    def __init__(self, feilname):
        self.feilname = os.getcwd() + os.sep + "data" + os.sep + feilname

    # 读取文件
    def read_yaml(self):
        with open(self.feilname, "r", encoding="utf-8") as f:
            return yaml.load(f)

    def read_yaml1(self):
        with open("../data/login_data.yaml", "r", encoding="utf-8") as f:
            return yaml.load(f)
            # return yaml.load(f)

if __name__ == '__main__':
    arrs = []
    for data in ReadYaml(" ").read_yaml1().values():
        arrs.append((data.get("username"), data.get("password"), data.get("expect_result"), data.get("expect_toast")))
    print(arrs)