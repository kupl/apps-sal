class Dog ():
    def __init__(self, breed):
        self.breed = breed


snoopy = Dog("Beagle")

Dog.bark = lambda self: "Woof"

scoobydoo = Dog("Great Dane")
