class WordDictionary:

    def __init__(self):
        self.dct = set()

    def add_word(self, word):
        self.dct.add(word)

    def word_match(self, w, s):
        if len(w) != len(s):
            return False
        try:
            for (i, c) in enumerate(s):
                if c != '.' and c != w[i]:
                    return False
            return True
        except:
            return False

    def search(self, s):
        for w in self.dct:
            if self.word_match(w, s):
                return True
        return False
