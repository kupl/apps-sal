class Cat(Animal):
    #your code here
    def __init__(self, cat):
        self.Animal = cat
    
    def speak(self):
        return self.Animal + ' meows.'
