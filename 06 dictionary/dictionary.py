a = {'name': 'Mamun', 'nickname': 'Maateen', 'email': 'maateen@outlook.com', 'phone': '01711223344'}
print (a['name'])

a['name'] = 'Mamun Sarkar'
print (a['name'])

b = {'hometown': 'Barisal', 'fav_poet': 'Nazrul'}
a.update(b)
print (a)

del a['phone']
print (a)

b.clear()
print (b)

print ('name' in a)

print (a.items())
print (a.keys())
print (a.values())
