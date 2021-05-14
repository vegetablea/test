# -*- encoding=utf8 -*-
__author__ = "姜家豪"
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

# command = Android()
# print("唤醒:%s"% command.wake())
# print("手机里所有的app:%s"% command.list_app())

poco("com.sz01hotel.android.stg:id/tv_name").click()
poco(text="昵称").click()
text(r"豪")
poco("com.sz01hotel.android.stg:id/tv_back").click()
poco("com.sz01hotel.android.stg:id/tv_back").click()
name = poco("com.sz01hotel.android.stg:id/tv_name").get_text()
print("name:",name)
assert_equal(name, "豪", "个人信息修改验证！")



