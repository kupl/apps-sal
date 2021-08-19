class Cat(Animal):

    def __init__(self, name):
        setattr(self, 'speak', lambda: '{} meows.'.format(name))
