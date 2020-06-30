#!/usr/bin/python3
import pprint, pickle

# 使用pickle模块从文件中重构python对象
# pkl_file = open('data.pkl', 'rb')
#
# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)
#
# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)
#
# pkl_file.close()

# pkl_file = open('data.pkl', 'rb')
#
# data = pickle.load(pkl_file)
#
# print(data)
# data1 = pickle.load(pkl_file)
#
# print(data1)

with open('data.pkl', 'rb') as pkl_file:
    data = pickle.load(pkl_file)
    print(data)
