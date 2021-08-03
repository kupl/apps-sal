class Dog ():
    def __init__(self, bark):
        self.bark = "Woof"


snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")

scoobydoo.bark = lambda: "Woof"
