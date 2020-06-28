var1 = ["1", 2, "object", 2020]

print(len(var1))

# print(max(var1))
"""
Traceback (most recent call last):
  File "C:/Users/GG/PycharmProjects/LearnNotes/base_demo/list_demo.py", line 5, in <module>
    print(max(var1))
TypeError: '>' not supported between instances of 'int' and 'str'
"""

vec = [2, 4, 6]
print([{3 * x} for x in vec])

print([[x, x ** 2] for x in vec])
print([[x, x * 2] for x in vec])

print([3 * x for x in vec if x > 3])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon for weapon in freshfruit])
# strip()  去除空格
print([weapon.strip() for weapon in freshfruit])

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]

print([x * y for x in vec1 for y in vec2])
print([x + y for x in vec1 for y in vec2])

# round 精度显示，
print([str(round(355 / 113, i)) for i in range(0, 6)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])

for i in range(4):
    print("---")
    for row in matrix:
        print(row[i])
