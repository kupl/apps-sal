class Dog ():
    def __init__(self, breed):
        self.breed = breed


snoopy = Dog("Beagle")
scoobydoo = Dog("Great Dane")
scoobydoo.bark = snoopy.bark = lambda: "Woof"
