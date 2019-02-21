#EVERYTHING is an object
#lists, strings, numbers, tuples, floats,....etc are instances of that class
print(type([])) # => class of list


#self is referring to each unique instance of the class
class Dog():
    totalDogs = 0
    def __init__(self, name="", age=1, color=""): #self is this in Javascript
        self.name = name
        self.age = age
        self.color = color
        
        Dog.totalDogs += 1 #accessing totalDogs

    def bark_hello(self): #in JS, we used arrow functions. in py, we need to pass self in the method to bind.
        print('Woof! I am called', self.name, 'and I am', self.age)

    def getTotalDogs(self):
        print('There are ', Dog.totalDogs, 'dogs made from this class')

franklin = Dog('Franklin', 4)
gunner = Dog('Gunner', 2)
suzy = Dog()
mateo = Dog()
print(gunner.bark_hello())
print(suzy.bark_hello())

print(franklin)
print(franklin.name) #with instances of a class, we can use dot notation to access properties
franklin.bark_hello()
gunner.getTotalDogs() # => 4 dogs

## Instance Variables - each that that is attached to self is an instance var
    #example: franklin, gunner, suzy are instance vars.

#Class Var = attached to the class itself. only 1 single thing 
#that exists for the entire class
    #example: totalDogs = 0 (at top of class)


class Parent():
    def __init__(self):
        self.first_name = 'Jim'
        self.last_name = 'Rocks'

    def hello(self):
        print(f'Hey I am {self.first_name}, nice to meet you!')
    
    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self, name):
        self.first_name = name
        return self.first_name
    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])
    
class Child(Parent): #extends in JS. we just plug in Parent class in arg
    def __init__(self):
        Parent.__init__(self) #super in JS.
        self.first_name = "Tzuyu"
        print('Child init', self)
    
    def hello(self):
        print(f'I am {self.first_name}, busy in class')    #can overwrite the

mom = Parent()
daughter = Child()

mom.hello()
daughter.hello()
print(daughter.last_name)
