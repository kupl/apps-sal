class Cat(Animal):
    #your code hereaa
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f'{self.name} meows.'
