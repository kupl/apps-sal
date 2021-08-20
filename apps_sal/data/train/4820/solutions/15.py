class Cat(Animal):

    def __init__(self, animal):
        self.animal = animal
        self.word = 'meows.'

    def speak(self):
        return self.animal + ' ' + self.word
