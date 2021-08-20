class Dog:

    def __init__(self, breed: str):
        self.breed = breed

    @staticmethod
    def bark() -> str:
        return 'Woof'


(snoopy, scoobydoo) = (Dog('Beagle'), Dog('Great Dane'))
