class Dog ():
    def __init__(self, breed):
        self.breed = breed
        self.bark = lambda: "Woof"


snoopy, scoobydoo = Dog("Beagle"), Dog("Great Dane")
