if True:
    print('Its True')
elif not True:
    print('fsdf')
else:
    print('sdfsd')

mylist = [1,2,3,4,5,6]
for list in mylist:
    print(list)

mylist = [(1,2), (3,4), (5,6)]
for (a,b) in mylist:
    print(a)
    print(b)

d = {'k1': 1, 'k2' : 2, 'k3': 3}
for key,value in d.items():
    print(value)