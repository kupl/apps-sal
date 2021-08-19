class Cat(Animal):

    def __init__(self, Animal=''):
        self.animal = Animal

    def speak(self):
        return self.animal + ' meows.'
