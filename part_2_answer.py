#!/usr/bin/env python
# coding=utf-8

'''
    考验判断、循环
'''

if __name__ == '__main__':
    # 循环：从1000到3000
    for i in range(1000, 3000):
        # 如果年份能够被4整除
        if i % 4 == 0:
            # 如果年份不能够被100整除
            if i % 100 != 0:
                # 输出年份
                print(i)
            # 如果年份能够被100整除
            else:
                # 如果年份能被400整除
                if i % 400 == 0:
                    # 输出年份
                    print(i)
                # 如果年份不能被400整除
                else:
                    # 什么也不做
                    pass
