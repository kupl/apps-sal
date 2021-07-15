class SelfClosing:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        self.obj.open_jar()
        return self.obj

    def __exit__(self, *_):
        self.obj.close_jar()
