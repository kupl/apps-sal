class BigDog:

    def __init__(self, breed):
        self.breed = breed


class Dog(BigDog):

    @staticmethod
    def bark():
        return 'Woof'


snoopy = Dog('Beagle')
snoopy.bark = lambda: 'Woof'
scoobydoo = Dog('Great Dane')
