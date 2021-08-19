from collections import defaultdict
from functools import reduce


class StreamChecker:

    def __init__(self, words: List[str]):

        def Trie():
            return defaultdict(Trie)
        self.trie = Trie()
        for word in words:
            reduce(dict.__getitem__, word, self.trie)['#'] = True
        self.waiting = []

    def query(self, letter: str) -> bool:
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any(('#' in node for node in self.waiting))
