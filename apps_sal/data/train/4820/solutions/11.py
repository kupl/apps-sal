class Cat(Animal):
    
    def __init__(self, name):
        self.cat_name = name
    
    def speak(self):
        return f"{self.cat_name} meows."
