"""
* We need to write self in classes so as to tell python which dog we are referring to.
"""
# = = = = = = = = = = =  = = == = == = = = = = =
class Dog: # Class -> Dog
    def __init__(self, name = None, age = None): # Special Method.   ||  It will be called on line 30    ||  trial1 = Dog()
        self.name = name # defined attribute name of the class dog
        self.age = age # defined attribute age for the class dog

    # For PART - 1
    def bhau(self, x=1):
        return "Bhau" *x
    def bark(self): # Method of class Dog
        print('bark')
    
    # For PART - 2
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def set_age(self,age):
        self.age = age
# = = = = = = = = = = =  = = == = == = = = = = =

# # # # # # # # # # # # # # # # # #
print("PART - 1")

trial1 = Dog() # A instance of class dog

trial1.bark() # Calling the method bark  ||  bark   
print(trial1.bhau(5)) # Calling method bhau  ||   BhauBhauBhauBhauBhau   

print(type(trial1)) # <class '__main__.Dog'>    ||    The file is the main class so __main__

# # # # # # # # # # # # # # # # # #
print("PART - 2")

silky = Dog("silky",14) # creating a new instance(silky) of the class Dog
print(silky.get_name()) # printing output of the method get_name of instance silky   ||  silky
print(silky.get_age())  # printing output of the method get_age of instance silky   ||  14

jimmy = Dog("jimmy",6)  # creating a new instance(jimmy) of the class Dog
print(jimmy.get_name()) # printing output of the method get_name of instance jimmy   ||  jimmy
print(jimmy.get_age())  # printing output of the method get_age of instance jimmy    ||  6

jimmy.set_age(11)
print(jimmy.get_age())  # printing again the output of the method get_age of instance jimmy    ||  11
