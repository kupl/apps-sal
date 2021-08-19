class Dog:

    def __init__(self, breed):
        self.breed = breed
        self.bark = 'Woof'


snoopy = Dog('Beagle')
snoopy.bark = lambda: 'Woof'
scoobydoo = Dog('Great Dane')
scoobydoo.bark = lambda: 'Woof'
