#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
file: client.py
socket client
"""

import socket
import sys


def socket_client():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('162.105.183.58', 6666))

    print(s.recv(1024))
    while 1:
        data = input('please input work: ')
        s.send(bytes(data, "utf-8"))
        print(s.recv(1024))
        if data == 'exit':
            break
    s.close()


if __name__ == '__main__':
    socket_client()
