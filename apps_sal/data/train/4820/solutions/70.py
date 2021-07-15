class Cat(Animal):
    def __init__(self, animal):
        self.name = animal
    
    def speak(self):
        return "{0} meows.".format(self.name)
