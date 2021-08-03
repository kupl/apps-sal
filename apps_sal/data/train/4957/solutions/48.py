class Dog ():
    def __init__(self, breed):
        self.breed = breed

    def bark(self):
        s = ''
        for i in self.breed:
            s = 'Woof'
        return s


snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")
