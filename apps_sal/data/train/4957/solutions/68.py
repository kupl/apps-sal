class Dog ():
    def __init__(self, breed):
        self.breed = breed


snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"


class Dog(Dog):
    def bark(self):
        return "Woof"


scoobydoo = Dog("Great Dane")
