def say_hello(name='Default'):
    print(f'hello {name}')

say_hello()

def myfunc(*args):
    return sum(args) * 0.05

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('fruit {}'.format(kwargs['fruit']))   # kwargs is converted to dictionary (key word arg)

myfunc(fruit='apple', veggie = 'lettuce') # {'fruit: 'apple', 'veggie': 'lettuce}\


def square(num):
    return num**2

my_nums = [1,2,3,4,5]
for item in map(square, my_nums):
    print(item)

