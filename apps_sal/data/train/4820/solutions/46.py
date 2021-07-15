class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " meows."
    def __str__(self):
        return " {}".format(self.speak)

