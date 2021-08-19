class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'noise makes a noise.'


class Cat(Animal):

    def speak(self):
        return self.name + ' meows.'
