class Cat(Animal):

    def __init__(self, cat_n):
        self.cat_n = cat_n

    def speak(self):
        return self.cat_n + ' meows.'
