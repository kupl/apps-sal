class SelfClosing(object):

    def __init__(self, closable):
        self.closable = closable

    def __enter__(self):
        self.closable.open_jar()
        return self.closable

    def __exit__(self, *args):
        self.closable.close_jar()
