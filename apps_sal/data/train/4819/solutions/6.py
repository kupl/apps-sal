class SelfClosing(object):

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        self.obj.open_jar()
        return self.obj

    def __exit__(self, *funcs):
        self.obj.close_jar()
