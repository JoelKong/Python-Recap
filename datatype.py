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