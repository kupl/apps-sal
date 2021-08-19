from collections import defaultdict
from functools import reduce


class StreamChecker:

    def __init__(self, words: List[str]):
        # O(N x M)

        # self.s = \"\"
        # self.dic = defaultdict(set)
        # for w in words:
        #     self.dic[w[-1]].add(w)

        def Trie(): return defaultdict(Trie)
        self.trie = Trie()
        for word in words:
            reduce(dict.__getitem__, word, self.trie)['#'] = True
        self.waiting = []

    def query(self, letter: str) -> bool:
        # O(M) where M is a max word length.

        # self.s += letter
        # return any(self.s.endswith(w) for w in self.dic[letter])

        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any('#' in node for node in self.waiting)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
