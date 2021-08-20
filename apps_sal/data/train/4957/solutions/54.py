class Dog:

    def __init__(self, breed):
        self.breed = breed
        self.bark = lambda: 'Woof'


snoopy = Dog('Husky')
scoobydoo = Dog('Great Dane')
