class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
    
    def speak(self):
        print("Sorry bro I don't know what I say")


class Dog(Pet):    
    def speak(self):
        print("Bark")
    
class Cat(Pet): 
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print('meow')
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.")
    
class Fish(Pet):
    pass
    

p = Pet("Silky", 19)
p.show()

c = Cat("Jellie", 14, 'grey')
c.show()
c.speak()

d = Dog("Rocky", 16)
d.show()
d.speak()

f = Fish("Bubbly", 5)
f.show()
f.speak()