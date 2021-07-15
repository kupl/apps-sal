class Cat(Animal):
    def __init__ (self, name):
        self.name = name
    
    def speak (self):
        meows = 'meows.'
        return (self.name + " " + meows)
