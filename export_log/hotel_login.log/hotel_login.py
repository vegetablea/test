# -*- encoding=utf8 -*-
__author__ = "hao"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# from appium import webdriver
auto_setup(__file__)


poco("零壹酒店(Staging)").click()
poco("com.sz01hotel.android.stg:id/tv_mine").click()

def login1():
    poco("com.sz01hotel.android.stg:id/tv_login").click()
    poco("com.sz01hotel.android.stg:id/et_phone").click()
    text("18682436420")
    poco("com.sz01hotel.android.stg:id/tv_login").click()
    poco("com.sz01hotel.android.stg:id/input_valid_code").click()
    text("123456")

def logout():
    poco("com.sz01hotel.android.stg:id/tv_setting").click()
    poco(text="安全退出").click()
    poco("com.sz01hotel.android.stg:id/bt_right").click()

aa = poco("com.sz01hotel.android.stg:id/tv_login")
if aa:
    login1()
else:
    logout()
    login1()






