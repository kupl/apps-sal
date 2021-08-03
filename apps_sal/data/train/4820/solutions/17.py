class Cat:

    def __init__(self, name):
        super().__init__()
        self.name = name

    def speak(self):
        return f"{self.name} meows."
