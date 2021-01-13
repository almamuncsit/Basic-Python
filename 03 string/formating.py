a = 23
b = 3.2352354
c = 'Bangladesh'

print("Int %d" % a)
print("Float %.2f" % b)
print("Country %s" % c)


a = input()
b = input()

print("Input are : ", a, " and ", b)
print("Input are : %s and %s" % (a, b))

print(a + ' ' + b)
c = '-'.join((a, b))
print(c)
