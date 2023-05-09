def create_cubes(n):        # without yield we have to make a list then append which will take up O(n) of memory but with yield is O(1)
    for x in range(n):
        yield x**3

for x in create_cubes(10):
    print(x)



def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for number in gen_fibon(10):
    print(number)



def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()
print(next(g))

s = 'hello'
s_iter = iter(s)
next(s_iter)