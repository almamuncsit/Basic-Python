A = {'orange', 'banana', 'pear', 'apple', 'apple'}
print(type(A))
print(A)

A.add("where")
print (A)

#A.update('banana', 'Mango')
#print (A)

A.remove("where")
print (A)

A.discard("where")
print (A)

B = set('apple')
print(type(B))
print(B)