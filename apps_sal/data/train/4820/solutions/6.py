class Cat(Animal):
    """ Animal: Cat """

    def __init__(self, name: str):
        """ Prepare data. """
        self.name = name

    def speak(self) -> str:
        """ Say my name! """
        return f'{self.name} meows.'
