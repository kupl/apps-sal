class Cat(Animal):

    def __init__(self, saying):
        self.saying = saying

    def speak(self):
        return self.saying + ' meows.'
