"""
The instructions say to use method prototypes which don't exist in Python.
Instead, we could monkey patch the internal __dict__ of the parent class, like
the example in [1], but this isn't very Pythonic, so I've subclassed instead.

[1]: http://stackoverflow.com/a/33033631/149428
"""


class Dog(object):

    def __init__(self, breed):
        self.breed = breed


class BarkingDog(Dog):

    def bark(self):
        return 'Woof'


snoopy = BarkingDog('Beagle')
scoobydoo = BarkingDog('Great Dane')
