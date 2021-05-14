#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-02-23 13:33
# @Author  : hao
# @File    : my_runner.py
# @Desc    :
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from airtest.cli.runner import AirtestCase, run_script
from argparse import *
import airtest.report.report as report
import jinja2
import shutil
import os
import io

class CustomAirtestCase(AirtestCase):
    # @classmethod
     # def setUpClass(cls):
     #     super(CustomAirtestCase,cls).setUpClass()


     def setUp(self):
        print("custom setup")
        super(CustomAirtestCase, self).setUp()

     def tearDown(self):
         print("custom tearDown")
         super(CustomAirtestCase, self).setUp()

     def run_air(self, root_dir='', device=[], scriptname='air_case'):
         # 用例目录
         script_path = root_dir + "/" + scriptname
         # 聚合结果
         results = []
         # 创建log文件
         root_log = root_dir + '/' + 'log'
         if os.path.isdir(root_log):
             shutil.rmtree(root_log)
         else:
             os.makedirs(root_log)
             print(str(root_log) + '  is created')

         # 创建export_log文件
         export_log = root_dir + '/' + 'export_log'
         if os.path.isdir(export_log):
             shutil.rmtree(export_log)
         else:
             os.makedirs(export_log)
             print(str(export_log) + '  is created')

         for f in os.listdir(script_path):
             if f.endswith(".air"):
                 # f为.air案例名称：login.air
                airName = f
                script = os.path.join(script_path, f)
                # airName_path为.air的全路径/Users/zhangxue/Documents/study/airtest_fppui/air_case/login.air
                print("当前运行脚本路径：" + str(script))
                # 日志存放路径和名称：/Users/zhangxue/Documents/study/airtest_fppui/log/login/log.html
                log = os.path.join(root_dir, 'log' + '/' + airName.replace('.air', ''))
                print("log路径：" + str(log))
                if os.path.isdir(log):
                  shutil.rmtree(log)
                else:
                  os.makedirs(log)
                  print(str(log) + '  is created')
                # global args
                args = Namespace(device=device, log=log, recording=None, script=script, compress=1)
                try:
                  run_script(args, AirtestCase)
                except:
                  pass
                finally:
                  export_output_file = os.path.join(export_log + "/" + airName.replace('.air', '.log') + '/log.html')
                  rpt = report.LogToHtml(script_root=script, log_root=log, export_dir=export_log)
                  rpt.report("log_template.html", output_file=export_output_file)
                  result = {}
                  result["name"] = airName.replace('.air', '')
                  result["result"] = rpt.test_result
                  results.append(result)

                # 生成聚合报告
                env = jinja2.Environment(
                loader=jinja2.FileSystemLoader(root_dir),
                extensions=(),
                autoescape=True
                )
                template = env.get_template("summary_template.html", root_dir)
                html = template.render({"results": results})
                output_file = os.path.join(export_log, "summary.html")
                with io.open(output_file, 'w', encoding="utf-8") as f:
                    f.write(html)
                print(output_file)


if __name__ == '__main__':
        test = CustomAirtestCase()
        root = os.path.abspath(".")
        print("root_path路径：  " + root)
        device = ['']

        test.run_air(root)
