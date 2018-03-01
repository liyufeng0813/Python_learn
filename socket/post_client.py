# !/usr/bin/python
# -*- coding:utf-8 -*- 

import socket
import os

"""发送文件到post_server端。"""

sk = socket.socket()
sk.connect(('127.0.0.1', 8001))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    info = input('input (post|file_path):').strip()
    if info == 'exit':
        break
    command, path = info.split('|')
    file_path = os.path.join(BASE_DIR, path)
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)
    file_info = 'post|{}|{}'.format(file_name, file_size)
    sk.sendall(bytes(file_info, 'utf8'))    # send file infomation

    f = open(file_path, 'rb')
    has_sent = 0
    while has_sent != file_size:
        data = f.read(4096)
        sk.sendall(data)
        has_sent += len(data)
    f.close()
    data = sk.recv(4096)
    print(data.decode('utf8'))

sk.close()
