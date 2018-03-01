# !/usr/bin/python
# -*- coding:utf-8 -*-

import subprocess


a = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE)
# stdout=subprocess.PIPE 把进程挪到a中,
print(a)
print(a.stdout.read().decode('gbk'))