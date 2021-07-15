class SelfClosing:
    def __init__(self, cookie_jar):
        self.cookie_jar = cookie_jar
        self.cookie_jar._is_open = True
    
    def __enter__(self):
        return self.cookie_jar
    
    def __exit__(self, exct, excv, tb):
        self.cookie_jar._is_open = False
