#!/usr/bin/env python
# coding=utf-8
'''
    进行班级数据处理
    考验数据操作
'''
'''

使用list和dict组合，把下列数据进行保存
并且输出，班级总分，男生总分，女生总分

姓名	性别	成绩
张三	男	96
李四	男	73
王五	女	100
陈六	男	26
邓七	女	62
'''


def insert_data(name, sex, score):
    return {'name': name, 'sex': sex, 'score': score}


if __name__ == '__main__':
    data_list = []
    data_list.append(insert_data('张三', '男', 96))
    data_list.append(insert_data('李四', '男', 73))
    data_list.append(insert_data('王五', '女', 100))
    data_list.append(insert_data('陈六', '男', 26))
    data_list.append(insert_data('邓七', '女', 62))
    score_all = 0
    score_male = 0
    score_female = 0
    for data in data_list:
        score_all += data['score']
        if data['sex'] == '男':
            score_male += data['score']
        if data['sex'] == '女':
            score_female += data['score']
    print('班级总分为{}'.format(score_all))
    print('男生总分为{}'.format(score_male))
    print('女生总分为{}'.format(score_female))
