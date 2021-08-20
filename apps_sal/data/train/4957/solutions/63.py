class Dog(object):

    def __init__(self, breed):
        self.breed = breed

    def bark(self):
        return 'Woof'


(snoopy, scoobydoo) = (Dog('Beagle'), Dog('Great Dane'))
