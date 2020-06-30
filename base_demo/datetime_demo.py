from datetime import date

now = date.today()
print(now)

birthday = date(1996, 2, 14)
age = now - birthday
print(age.days)
# print(age.year)
"""
Traceback (most recent call last):
  File "C:/Users/GG/PycharmProjects/LearnNotes/base_demo/datetime_demo.py", line 9, in <module>
    print(age.year)
AttributeError: 'datetime.timedelta' object has no attribute 'year'
"""

anniversary = date(2018, 12, 31)

a = now - anniversary

print(a.days)
