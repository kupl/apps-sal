class SelfClosing:

    def __init__(self, obj):
        self.object = obj

    def __enter__(self):
        self.object._is_open = True
        return self.object

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.object._is_open = False
