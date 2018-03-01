# !/usr/bin/python
# -*- coding:utf-8 -*-

import socket
import os

"""接收文件，并存储。"""


sk = socket.socket()
sk.bind(('127.0.0.1', 8001))
sk.listen(4)
print('waiting......')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    conn, addr = sk.accept()
    while True:
        data = conn.recv(4096)
        command, file_name, file_size = str(data, 'utf8').split('|')
        file_path = os.path.join(BASE_DIR, 'image', file_name)
        f = open(file_path, 'ab')
        has_received = 0
        while has_received != int(file_size):
            data = conn.recv(4096)
            f.write(data)
            has_received += len(data)
        f.close()
        conn.send('上传完成。'.encode('utf8'))

sk.close()
