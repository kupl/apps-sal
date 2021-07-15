class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + ' makes a ' + self.name +'.'

class Cat(Animal):
    def speak(self):
        return self.name + ' meows.'
