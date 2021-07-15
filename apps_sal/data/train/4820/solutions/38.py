class Cat(Animal):
    def __init__(self,name):
        self.name=name
    def speak(self):
        self.info=(self.name)+" meows."
        return(self.info)
