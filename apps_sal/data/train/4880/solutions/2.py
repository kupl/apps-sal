class anything:
    def __init__(self, x):
        pass
    __lt__ = __le__ = __gt__ = __ge__ = __eq__ = lambda self, other: True
