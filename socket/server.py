# !/usr/bin/python
# -*- coding:utf-8 -*-

import socket


sk = socket.socket()    # 实例化socket对象
sk.bind(('127.0.0.1', 8001))    # 绑定IP地址和端口
sk.listen(4)
print('waiting......')

while True:
    conn, addr = sk.accept()
    print(addr)

    while True:
        try:
            data = conn.recv(1024)
        except Exception:
            break

        if data is None: break
        print(str(data, 'utf8'))
        info = input('>>>')
        conn.send(bytes(info, 'utf8'))

sk.close()


#socket 参数
#type:
    # type = SOCK_STREAM : TCP协议
    # type = SOCK_DGRAM  : UDP协议
#family:
    # family = AF_INEF  : 服务器之间的通信
    # family = AF_INEF  : IPv6
    # family = AF_UNIX  : Unix不同进程间的通信