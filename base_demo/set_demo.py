a = set("abcdrfghijklmn")
print(a)

b = {x for x in 'abracadabra' if x not in 'abc'}

print(b)

print("r" in b)

b.clear()
print(b)
