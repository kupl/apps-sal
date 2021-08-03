class Dog(object):
    def bark(self):
        return "Woof"
    #Dog.bark = bark

    def __init__(self, breed):
        self.breed = breed


#Dog.bark = bark
snoopy = Dog("Beagle")


scoobydoo = Dog("Great Dane")
