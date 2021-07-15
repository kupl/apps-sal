class Cat(Animal):
    """
    Extend Animal class and replace speak method
    """
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + ' meows.'
