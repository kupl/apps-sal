from itertools import zip_longest


class WordDictionary:

    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def search(self, pattern):
        return any(all((a and b == '.') or a == b for a, b in zip_longest(word, pattern)) for word in self.words)
