#!/usr/bin/env python
# coding=utf-8
'''
    进行学生成绩操作
    考验list、tuple、dict、set操作
'''

if __name__ == '__main__':
    # 定义一个空list
    user_list = []
    # 使用tuple向list内保存信息“张三成绩是10分”
    user_list.append(('张三', 10))
    # 使用tuple向list内保存信息“李四成绩是10分”
    user_list.append(('李四', 20))
    # 使用tuple向list内保存信息“王五成绩是10分”
    user_list.append(('王五', 30))
    # 使用tuple向list内保存信息“陈六成绩是10分”
    user_list.append(('陈六', 10))
    # 使用tuple向list内保存信息“邓七成绩是10分”
    user_list.append(('邓七', 20))
    # 定义一个空的dict
    user_data = {}
    # 利用循环来遍历list
    for name, score in user_list:
        # 把list里的数据转成 key=学生名称，value=学生成绩 的键值对，保存在dict里
        user_data[name] = score
    # 定义一个空的set
    score_list = set()
    # 利用循环来遍历dict
    for _, value in user_data.items():
        # set来保存分数
        score_list.add(value)
    # 输出分数的种类数量，按照要求自行替换xxx
    print('班级这次所有的分数有{}种数值'.format(len(score_list)))
