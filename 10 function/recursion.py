
def count(i):
    print (i)
    i += 1
    if i == 5:
        return
    count(i)

count(1)


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print (factorial(5))
