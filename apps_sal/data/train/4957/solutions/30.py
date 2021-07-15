class Dog ():
    bark = None

    def __init__(self, breed):
        self.breed = breed
    
    @property
    def bark(self):
        return Dog.bark
        
    @bark.setter
    def bark(self, func):
        Dog.bark = func  
    
snoopy = Dog("Beagle")

snoopy.bark = lambda x: "Woof"

scoobydoo = Dog("Great Dane")
