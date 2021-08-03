class Dog ():
    def __init__(self, breed):
        self.breed = breed
        self.message = "Woof"

    def bark(self):
        return self.message


snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")
