class Cat(Animal):
    s = ""
    
    def __init__(self, s):
        self.s = s
        
    def speak(self):
        return self.s + " meows."
