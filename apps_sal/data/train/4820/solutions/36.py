class Cat(Animal):
    def __init__(self,name):
        Animal.__init__(self, name)
    def get_name(self):
        return self.name
    def speak(self):
        return self.name + " meows."
