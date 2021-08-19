class Dog(object):

    def bark(self):
        return 'Woof'

    def __init__(self, breed):
        self.breed = breed


snoopy = Dog('Beagle')
scoobydoo = Dog('Great Dane')
