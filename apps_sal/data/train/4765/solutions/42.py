class Hero(object):
    def __init__(self, name=None):  # Pass name=None to get None if no argument is passed
        if name == None:  # Assignm values according to the appropriate arguments passed to the object
            self.name = 'Hero'
        else:
            self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
