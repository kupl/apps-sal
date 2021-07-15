class SelfClosing:
    def __init__(self, jar):
        self.jar = jar
    def __enter__(self):
        self.jar._is_open = True
        return self.jar
    def __exit__(self, a, b, c):
        self.jar._is_open = False
