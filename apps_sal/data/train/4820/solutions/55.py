class Cat(Animal):
    # your code here
    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        return self.name + ' meows.'


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'noise makes a noise.'
