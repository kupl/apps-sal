class SelfClosing(object):

    def __init__(self, jar):
        self._jar = jar
        
    def __enter__(self):
        self._jar.open_jar()
        return self._jar

    def __exit__(self, *args):
        self._jar.close_jar()

