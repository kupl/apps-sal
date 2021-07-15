class Dog ():
    def __init__(self, breed, sound):
        self.breed = breed
        self.bark = sound

def sound(): return 'Woof'

snoopy = Dog("Beagle", sound)
scoobydoo = Dog("Great Dane", sound)
