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