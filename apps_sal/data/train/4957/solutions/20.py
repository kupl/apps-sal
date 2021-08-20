class Dog(object):

    def __init__(self, breed):
        self.breed = breed
        self.bark = lambda: 'Woof'

    def bark(self):
        return 'Woof'


snoopy = Dog('Beagle')
scoobydoo = Dog('Great Dane')
