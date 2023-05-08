class Dog():
    species = 'mammal'

    def __init__(self, breed):
        self.breed = breed

    def bark(self):
        print(f"WOOF! My name is {self.name}")

my_dog = Dog('Golden Retriever')
print(my_dog.breed)

class Animal():
    def __init__(self):
        print('a')
    
    def who(self):
        print('fsdf')

class Cat(Animal):           #to extend inheritance
    def __init__(self):
        Animal.__init__(self)



class Book():
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):          #if printing the class or check str(instance)
        return f"{self.title} fsdf"
    
    def __len__(self):          #if checking the len of the class or check len(instance)
        return self.pages
    
    def __del__(self):
        print('deleted')
    
del b