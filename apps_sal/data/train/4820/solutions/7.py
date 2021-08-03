class Cat(Animal):
    def __init__(self, name):
        super().__init__(self)
        self.name = name

    def speak(self):
        return self.name + " meows."
