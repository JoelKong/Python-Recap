print("Hello world")

a = 30

print(type(a))
a = "hello"
print(len(a))
a[-3]

mystring = 'abcdefghijk'
print(mystring[2:])
print(mystring[:3])
print(mystring[3:6])
print(mystring[::2])
print(mystring[::-1]) # reverse string 

name = "sam hello"
last_letters = name[1:]
"P" + last_letters 

name.upper()
name.split() # ['sam', 'hello'] split by white space
name.split('i') # remove the 'i' and then split until it hits the next 'i'
print('This is a string {}'.format('INSERTED'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print(f'hello {name}')

new_list = [1,2,3,4,5]
new_list.pop(-1)
new_list.append(6)
new_list.sort() # auto sort
new_list.reverse()

my_dict = {'key1': 2, 'key2': 3}
my_dict['key1']
my_dict.keys()
my_dict.values()
my_dict.items() #return tuple

t = (1,2,2,3)
t.count(2) # returns how many times 2 appears
t.index('a') #returns index when first encounter

my_set = set()
my_set.add(1)
my_set.add(2) #{1,2} unique values

myfile = open('myfile.txt')
myfile.read()
myfile.seek(0) #can call .read again after seek
myfile.readlines() #create lists based off next line
myfile.close()
with open('myfile.txt', mode='w') as my_new_file:
    contents = my_new_file.read()
myfile.write('hi')