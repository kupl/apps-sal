class Cat():  # Animal
    def __init__(self, name):
        self.name = str(name)       # T=cat([2, 4, 6]):    T.speak() -> '[2, 4, 6] meows.'

    def speak(self):
        return self.name + " meows."
