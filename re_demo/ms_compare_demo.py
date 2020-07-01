import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com'))  # 不在起始位置匹配
