class Dog:
    """ Animal: Dog. """

    def __init__(self, breed: str):
        """ Prepare data. """
        self.breed = breed
        self.bark = lambda: 'Woof'


snoopy = Dog('Beagle')
scoobydoo = Dog('Great Dane')
