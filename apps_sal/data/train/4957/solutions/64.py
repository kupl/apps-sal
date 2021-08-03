class Dog ():
    def __init__(self, bark):
        self.bark = bark


snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")
scoobydoo.bark = lambda: "Woof"
