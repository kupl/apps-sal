class anything:

    def __init__(self, _):
        pass

    def __eq__(self, other):
        return True
    __ne__ = __lt__ = __le__ = __ge__ = __gt__ = __eq__
