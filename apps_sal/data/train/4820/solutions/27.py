class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " meows."


cat = Cat("Mr Whiskers")
print(cat.speak())
