class Dog ():
    def __init__(self, breed):
        self.breed = breed


snoopy = Dog("Beagle")
scoobydoo = Dog("rogling")

snoopy.bark = lambda: "Woof"

scoobydoo.bark = lambda: "Woof"
