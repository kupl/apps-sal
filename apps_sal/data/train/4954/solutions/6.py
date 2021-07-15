from itertools import zip_longest
class WordDictionary:
    def __init__(self):
        self.d = set()

    def add_word(self, s):
        return self.d.add(s)

    def search(self, s):
        for w in self.d:
            if all((a==b or b == '.') and a for a,b in zip_longest(w,s)):
                return 1
        return 0
