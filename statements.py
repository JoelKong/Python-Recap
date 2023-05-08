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

for num in range(0,11,2):
    print(num)

list(range(0,11,2))

for item in enumerate('abcde'):
    print(item)

list1 = [1,2,3]
list2 = [4,5,6]

for item in zip(list1,list2):
    print(item)

min(list1)
max(list2)

#libraries
from random import shuffle
from random import randint
shuffle(mylist)
int(input('enter'))

mylist = [letter for letter in list1]