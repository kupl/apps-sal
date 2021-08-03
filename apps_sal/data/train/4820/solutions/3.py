class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        return f"{self.name} meows."
