#!/usr/bin/env python
# coding=utf-8
'''
    进行个人介绍
    考验输出、变量、数据类型、字符串
'''

if __name__ == '__main__':
    # 定义一个变量，值为你的姓
    last_name = 'a'
    # 定义一个变量，值为你的名
    first_name = 'b'
    # 定义一个变量，值为你的姓的变量和你的名的变量组合成的，你的姓名
    name = last_name + first_name
    # 定义一个值等于你的出生年份的变量
    year = 1000
    # 定义一个值等于你的出生月份的变量
    month = 3
    # 定义一个值等于你的出生日期的变量
    day = 1
    # 今年年份
    now_year = 2018
    # 定义一个变量，值由now_year和你的出生年份的变量计算出来的年龄
    age = now_year - year + 1
    # 把上面定义的变量名称替换format()的括号里面的xxx
    print('我叫{}'.format(name))
    print('{}年{}月{}日出生'.format(year, month, day))
    print('今年{}岁'.format(age))
