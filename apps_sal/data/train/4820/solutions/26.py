class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "{0} makes a {0}.".format(self.name)
class Cat(Animal):
    def speak(self):
        return "{} meows.".format(self.name)
