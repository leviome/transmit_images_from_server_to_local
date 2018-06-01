#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: liaoliwei
@contact: levio@pku.edu.cn
@file: BENJI.py
@time: 2018/6/1 13:43
"""
#coding:utf-8
from flask import request, Flask
import json
import numpy as np
import time
import cv2

app = Flask(__name__)

@app.route("/", methods=['POST'])
def get_frame():
    start_time = time.time()
    res = json.loads(request.data)
    print(type(res["image"]))
    b_data = bytes(res["image"], 'utf-8	')
    frame = eval(b_data.decode("utf-8"))   # dtype为int32
    frame = np.array(frame, dtype=np.uint8)
    cv2.imwrite('figure.png',frame)
    duration = time.time() - start_time
    print('duration:[%.0fms]' % (duration*1000))
    # cv2.imshow('hehe', frame)
    return '0000'

if __name__ == "__main__":
    app.run("162.105.183.180", port=8081)  #端口为8081
