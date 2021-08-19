import re


class WordDictionary:

    def __init__(self):
        self.words = set()

    def add_word(self, word):
        self.words.add(word)

    def search(self, pattern):
        pattern += '$'
        return any((re.match(pattern, word) for word in self.words))
