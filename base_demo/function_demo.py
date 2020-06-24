#!/usr/bin/python3

# 可写函数说明
def changeme(aa):
    "修改传入的列表"
    aa.append([1, 2, 3, 4])
    print("函数内取值: ", aa)
    return


# 调用changeme函数
mylist = [10, 20, 30]
print("函数外取值: ", mylist)
changeme(mylist)
print("函数外取值: ", mylist)


# 可写函数说明
def printinfo(arg1=100, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(11, 22, 33, 44)


# 可写函数说明
def printinfo1(*vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(vartuple)


# 调用printinfo 函数
printinfo1(11, 22, 33, 44)


def f(a, *, b, c):
    return a + b + c


print(f(1, b=2, c=3))

def d(a, /, b, c):
    return a + b + c


print(d(1, b=2, c=4))
print(d(1, 2, 4))
