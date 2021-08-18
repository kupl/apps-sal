class SelfClosing(object):
    def __init__(self, CookieJar):
        self.CookieJar = CookieJar

    def __enter__(self):
        self.CookieJar.open_jar()
        return self.CookieJar

    def __exit__(self, *args):
        self.CookieJar.close_jar()
