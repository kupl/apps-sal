class Cat(Animal):
    def __init__(self, name):
        self.name = str(name)
    
    def speak(self):
        return self.name + ' meows.'
