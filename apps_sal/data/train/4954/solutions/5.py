from collections import defaultdict
from re import compile, match


class WordDictionary(defaultdict):

    def __init__(self):
        super(WordDictionary, self).__init__(list)

    def add_word(self, s):
        self[len(s)].append(s)

    def search(self, s):
        p = compile(f'^{s}$')
        return any((match(p, w) for w in self[len(s)]))
