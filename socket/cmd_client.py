# !/usr/bin/python
# -*- coding:utf-8 -*- 

import socket


"""client: send cmd command; server: return the result of this command."""

sk = socket.socket()
sk.connect(('127.0.0.1', 8001))


while True:
    info = input('>>>')
    if info == 'exit':
        break
    sk.send(bytes(info, 'utf8'))
    data_len = int(str(sk.recv(4096), 'utf8'))
    print(data_len)
    sk.send(bytes('ok', 'utf8'))    # 用于解决粘包问题
    result = bytes()    # 初始化一个bytes，用于累计接收数据，并用于判断。

    while len(result) != data_len:  # 存在对方发送的数据过大，无法一次接收，所以循环接收数据。
        data = sk.recv(4096)
        result += data
    print(str(result, 'gbk'))

sk.close()
