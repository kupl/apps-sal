class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        speak = 'meows.'
        return str(self.name + ' ' + speak)
