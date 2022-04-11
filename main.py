# -*- coding: utf-8 -*-
import string
import random


def random_code():
    # 32位数字、符号、字母随机码
    # return ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 32))
    return ''.join(random.sample(string.ascii_letters + string.digits, 36))


if __name__ == '__main__':
    print(random_code())
