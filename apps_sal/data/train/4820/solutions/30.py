class Cat:
    def __init__(self,cat):
        self.name = cat
        self.call = self.name + ' meows.'
    
    def speak(self):
        return self.call
