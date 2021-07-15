class Dog:

    def __init__(self, breed):
        self.breed = breed
        
    def bark(self):
        return "Woof"
        
        
class Snoopy(Dog):

    def __init__(self, breed):
        Dog.__init__(self, breed)

    def bark(self):
        return self.bark
            
        
        
class Scooby(Dog):

    def __init__(self, breed):
        Dog.__init__(self, breed)

    def bark(self):
        pass #super(Dog, self).bark()


snoopy = Dog("Beagle")
snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")
