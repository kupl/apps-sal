import re


class WordDictionary:

    def __init__(self):
        self.d = {}

    def add_word(self, w):
        self.d[w] = True

    def search(self, k):

        if not '.' in k:
            return self.d.get(k, False)

        r = re.compile('^{}$'.format(k))
        return any(r.match(x) for x in self.d.keys())
