class Cat(Animal):
    def __init__(self, name, *args, **kwargs):
        assert isinstance(name, str)
        self.name = name

    def speak(self):
        return " ".join((self.name, 'meows.'))
