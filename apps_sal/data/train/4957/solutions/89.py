class Dog:

    def __init__(self, breed):
        self.breed = breed

    def bark(self, woof):
        print('Woof')


snoopy = Dog('Beagle')
snoopy.bark = lambda: 'Woof'
scoobydoo = Dog('Great Dane')
scoobydoo.bark = lambda: 'Woof'
