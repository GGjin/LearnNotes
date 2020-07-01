"""
A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。

日上三杆，A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。

B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。 。

C、D、E依次醒来，也按同样的方法拿鱼。

问他们台伙至少捕了多少条鱼?
"""

"""a = n
b = (a - 1) / 5 * 4
c = (b - 1) / 5 * 4
d = (c - 1) / 5 * 4
e = (d - 1) / 5 * 4

d = 
"""


def checkFishs(total, num):
    total = total / 4 * 5 + 1
    num -= 1
    if num > 0:
        if total % 4 == 0:
            return checkFishs(total, num)
        else:
            return False
    else:
        return int(total)


fish, total = 1, 1
while True:
    total = checkFishs(fish, 5)
    if total:
        break
    else:
        fish += 1

print("--->", fish)
print("--->", total)

# n = 1
# person1 = (n-1)/5
# person2 = (person1 * 4 -1) / 5
# person3 = (person2 * 4 -1) / 5
# person4 = (person3 * 4 -1) / 5
# person5 = (person4 * 4 -1) / 5
#
# while True:
#
#     if int(person1) == person1 and int(person2) == person2 and int(person3) == person3 and int(person4) == person4 and int(person5) == person5:
#         break
#
#     else:
#         n += 1
#         person1 = (n-1)/5
#         person2 = (person1 * 4 -1) / 5
#         person3 = (person2 * 4 -1) / 5
#         person4 = (person3 * 4 -1) / 5
#         person5 = (person4 * 4 -1) / 5
#
# print('There are %d fish in total.' %n)


# # n个人总共捕鱼数量为：S = Kn^n-(n-1) K为正整数
# # 最后一个人分得鱼的数量为：S(n) = K(n-1)^(n-1)-1 K为正整数
#
# # 至少捕鱼数（即K为1）
# def min_fish(n):
#     return n ** n - (n - 1)
#
#
# if __name__ == '__main__':
#     n = int(input('请输入人数:'))
#     print('至少捕了{0}条鱼'.format(min_fish(n)))
