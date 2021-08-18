class Cat(Animal):
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "{} meows.".format(self._name)
