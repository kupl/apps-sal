class Cat(Animal):

    def __init__(self, Animal):
        self.Animal = Animal

    def speak(self):
        return f'{self.Animal} meows.'
