# !/usr/bin/python
# -*- coding:utf-8 -*- 

import socket


sk = socket.socket()
sk.connect(('127.0.0.1', 8001))

while True:
    info = input('>>>')
    if info == 'exit':
        break
    sk.send(bytes(info, 'utf8'))
    data = sk.recv(1024)
    print(str(data, 'utf8'))

sk.close()
