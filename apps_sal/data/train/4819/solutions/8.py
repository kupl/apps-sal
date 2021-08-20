class SelfClosing(object):

    def __init__(self, jar):
        self._jar = jar
        self.take = self._jar.take

    def __enter__(self):
        self._jar.open_jar()
        return self

    def __exit__(self, *a):
        self._jar.close_jar()


SelfClosing = type('SelfClosing', (object,), {'__init__': lambda s, j: (setattr(s, 'j', j), setattr(s, 'take', s.j.take))[0], '__enter__': lambda s: (s.j.open_jar(), s)[1], '__exit__': lambda s, *a: s.j.close_jar()})
