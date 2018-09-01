#!/usr/bin/python
#coding:utf-8

"""
@author: xuxin
@contact: xuxin8911@126.com
@software: PyCharm
@file: unit_conversion.py
@time: 2018/9/1 17:35
@python version: 3.6
"""
import re

def unit_conversion(string):
    '''
    将TB GB MB KB、 t g m B、 bytes等转换为MB，保留一位小数， 并去掉结尾单位
    :param old_data:
    :return:
    '''
    num = float(re.match("\d+\.?\d*", string).group())
    # 加strip()是为了适应数字和单位中间有空格情况： 123.4 MB
    unit = string.replace(str(num), '').strip().upper()
    if unit in ['B', 'BYTES']:
        num = num/1024/1024
    elif unit in ['K', 'KB']:
        num = num/1024
    elif unit in ['M', 'MB']:
        pass
    elif unit in ['G', 'GB']:
        num = num * 1024
    elif unit in ['T', 'TB']:
        num = num * 1024 * 1024
    num = float('%.1f'%num)
    print(num)
    return num



def main():
    unit_conversion('1524121.1234B')
    unit_conversion('1524121.1234KB')
    unit_conversion('1524121.1234 MB')
    unit_conversion('1524121.1234 T')


if __name__ == "__main__":
    main()
