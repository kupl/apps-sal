class Cat(Animal):

    def __init__(self, meows):
        self.meows = meows

    def speak(self):
        return f'{self.meows} meows.'
