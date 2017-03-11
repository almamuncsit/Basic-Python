my_list = [i**2 for i in range(20) if i%2 == 0]
print(my_list)

a_list = ['Maateen', 'Khan', 'Maksudur', 'a', 'b', 'c']
n_list = [i for i in a_list if len(i) > 1]
print (n_list)

a_list = ['name', 'country', 'career']
b_list = ['Mamun', 'Bangladesh', 'TeleTalk']
my_dec = {i : j for i, j in zip(a_list, b_list)}
print (my_dec)