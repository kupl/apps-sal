class Dog:

    def __init__(self, breed, bark):
        self.breed = breed
        self.bark = bark


snoopy = Dog('Beagle', 'Woof')
snoopy.bark = lambda: 'Woof'
scoobydoo = Dog('Great Dane', 'Woof')
scoobydoo.bark = lambda: 'Woof'
