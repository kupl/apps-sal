class Animal:
    def __init__(self, name, voice="meows"):
        if name == 'noise':
            self.voice = 'makes a noise'
        else:
            self.voice = voice
        self.name = name

    def speak(self):
        return f"{self.name} {self.voice}."


class Cat(Animal):
    pass
