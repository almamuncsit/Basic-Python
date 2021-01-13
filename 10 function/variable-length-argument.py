def add(*args):
    print(type(args))
    temp = 0
    for i in args:
        temp += i
    return temp


print (add(1, 5, 45, 25, 12, 3))


def add(**kwargs):
    print(type(kwargs))
    tmp = 0
    for key in kwargs:
        tmp = tmp + kwargs[key]
    return tmp


temp = add(a=1, b=2, c=3, d=4)
print(temp)
