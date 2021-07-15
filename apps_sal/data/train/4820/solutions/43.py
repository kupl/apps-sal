class Animal():
    def __init__(self, name):
        self.name = name
        self.word = "makes a noise"

    def get_name(self):
        return self.name

    def speak(self):
        return f"{self.name} {self.word}."


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.word = "meows"


cat = Cat("Whiskers")

print(cat.speak())
