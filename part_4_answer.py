#!/usr/bin/env python
# coding=utf-8
'''
    进行数字的大小比对
    考验函数
'''


# 定义一个函数，实现比较两个数，返回大的那个数值，等于则返回第一个
def number_max(first, second):
    if first >= second:
        return first
    else:
        return second


# 定义一个函数，实现比较两个数，返回小的那个数值，等于则返回第一个
def number_min(first, second):
    if first > second:
        return second
    else:
        return first


if __name__ == '__main__':
    # 按照输出文字的意思，自行替换xxx
    print('1和2比较，{}大'.format(number_max(1, 2)))
    # 按照输出文字的意思，自行替换xxx
    print('10和7比较，{}小'.format(number_min(10, 7)))
    # 按照输出文字的意思，自行替换xxx
    print('86和110比较，{}小'.format(number_min(86, 110)))
    # 按照输出文字的意思，自行替换xxx
    print('29和15比较，{}大'.format(number_max(29, 15)))
