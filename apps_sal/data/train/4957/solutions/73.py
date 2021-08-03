class Dog ():
    def __init__(self, breed):
        self.breed = breed


snoopy = Dog("Beagle")

Dog.bark = lambda x: "Woof"

scoobydoo = Dog("Great Dane")
