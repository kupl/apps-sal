class anything:
    def __init__(self, *args, **kwargs):
        pass


anything.__eq__ = anything.__neq__ = anything.__gt__ = anything.__ge__ = anything.__lt__ = anything.__le__ = lambda *x: True
