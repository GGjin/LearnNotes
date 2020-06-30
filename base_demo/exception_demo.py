# while True: print("aaa")


def test1():
    print('test1-1')
    print(num)
    print('test2-2')
def test2():
    print('test2-1')
    test1()
    print('test2-2')
def test3():
    try:
        print('test3-1')
        test1()
        print('test3-2')
    except Exception as result:
        print('检测出异常{}'.format(result))
    print('test3-2')
test3()
print('-------------')
test2()