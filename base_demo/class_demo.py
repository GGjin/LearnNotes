# class MyClass:
#     i = 1234
#
#     def f(self):
#         return "hello world"
#
#
# a = MyClass()
#
# print(a.i)
# print(a.f())

class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '这个人的名字是%s,已经有%d岁了！' % (self.name, self.age)


a = people('孙悟空', 999)
print(a)
