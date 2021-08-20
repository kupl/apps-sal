class Dog:

    def __init__(self, breed):
        self.breed = breed


snoopy = Dog('Beagle')
scoobydoo = Dog('Great Dane')
snoopy.bark = scoobydoo.bark = lambda: 'Woof'
