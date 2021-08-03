class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self): return "{} meows.".format(self.name)
