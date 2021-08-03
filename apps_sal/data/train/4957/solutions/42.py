class Dog ():
    def __init__(self, breed):
        self.breed = breed

    def breed(self):
        return self.breed


snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")

scoobydoo.bark = lambda: "Woof"
