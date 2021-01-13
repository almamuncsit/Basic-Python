l = ['one', 'two', 'three', 'four']
print (l[1])
print (l[1:3])
print (l[:4])
print (l[2:])

print(type(l))

l[1] = 2
print (l[1])

print (l)

l = l + ['eight', 'nine']
print (l)

del l[2]
print(l)

del l[-1]
print(l)
