#!/usr/bin/python3

# 打开一个文件

f = open("foo.txt", "w")

f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")

print("写入完成")
# 关闭打开的文件
f.close()
