class Cat(Animal):
    def __init__(self, name):
        self.cat_name = name

    def speak(self):
        return self.cat_name + ' ' + 'meows.'
