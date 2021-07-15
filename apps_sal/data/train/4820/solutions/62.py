class Cat(Animal):
    def __init__(self, name):
        self.name = name
    
    speak = lambda self: "{} meows.".format(self.name)
