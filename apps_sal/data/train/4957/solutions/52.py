class Dog:
    _bark = 'Woof'

    def __init__(self, breed):
        self.breed = breed

    def bark(cls):
        return cls._bark


snoopy = Dog('Beagle')
snoopy.bark = lambda: 'Woof'
scoobydoo = Dog('Great Dane')
