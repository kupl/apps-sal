class Cat(object):
    def __init__(self, animal):
        self.animal = animal

    def speak(self):
        return '{} meows.'.format(self.animal)
