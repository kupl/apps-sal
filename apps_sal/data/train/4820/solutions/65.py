class Cat(Animal):

    def ___init__(self, s):
        self.name = s

    def speak(self):
        return '{} meows.'.format(self.name)
