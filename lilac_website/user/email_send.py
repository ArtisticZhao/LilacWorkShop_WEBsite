# coding: utf-8
'''
本模块用于发送验证邮件
'''
from random import Random  # 用于生成随机码


# 生成随机字符串
def random_str(randomlength=20):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str
