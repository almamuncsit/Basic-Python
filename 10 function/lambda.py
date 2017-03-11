sum = lambda a, b: a + b
print(sum(50, 12))
print((lambda a, b: a + b)(12, 12))


def my_function(func, arg1, arg2):
    return func(arg1, arg2)

print(my_function(lambda a, b : a + b, 10, 20))