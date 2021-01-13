def func(a, b, c):
    print("a is : %d" % a)
    print("b is : %d" % b)
    print("c is : %d" % c)
    return a + b + c


print("sum is %d" % func(10, 15, 20))

print(func(b=10, c=15, a=20))


def add(a, b=10):
    return a + b


print("Add is %d" % add(5))

