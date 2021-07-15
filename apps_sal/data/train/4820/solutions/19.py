class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        if self.name == "noise":
            return self.name+ " makes a noise."
        return self.name+" meows."
    
class Cat(Animal):
    pass

