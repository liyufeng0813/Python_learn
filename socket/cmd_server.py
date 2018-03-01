# !/usr/bin/python
# -*- coding:utf-8 -*- 

import socket
import subprocess


sk = socket.socket()
sk.bind(('127.0.0.1', 8001))
sk.listen(4)
print('waiting......')

while True:
    conn, addr = sk.accept()
    print(addr)

    while True:
        try:
            data = conn.recv(4096)
        except Exception:
            break

        if data is None:
            break

        obj = subprocess.Popen(data.decode('utf8'), shell=True, stdout=subprocess.PIPE)     # stdout=subprocess.PIPE: 把这个进程挪到了obj对象的进程中，这样就可以通过obj这个对象读到这个进程运行的结果以及其他信息。
        cmd_result = obj.stdout.read()
        cmd_result_len = bytes(str(len(cmd_result)), 'utf8')
        conn.sendall(cmd_result_len)    # 发送数据长度。
        conn.recv(1024)   # 用于解决粘包问题，连着两个send可能发生粘包。
        print(cmd_result_len)
        conn.sendall(cmd_result)

sk.close()
