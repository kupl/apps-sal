class anything(object):

    def __init__(self, foo):
        pass

    def __eq__(self, other):
        return True
    __ne__ = __lt__ = __le__ = __gt__ = __ge__ = __eq__
