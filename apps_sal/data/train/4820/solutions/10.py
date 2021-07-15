class Cat(Animal):
    def __init__(self,name):
        self.name = name
        #self.speak = f"{name} meows"
        
    def speak(self):
        return f"{self.name} meows."

