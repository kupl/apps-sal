class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
    
    def speak(self):
        return f"{self.name} meows."
