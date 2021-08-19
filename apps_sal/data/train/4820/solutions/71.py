class Cat:

    def __init__(self, name='Chonky'):
        self.name = name

    def speak(self):
        return '{} meows.'.format(self.name)
