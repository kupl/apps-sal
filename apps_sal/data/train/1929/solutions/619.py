from collections import defaultdict


class TrieNode:

    def __init__(self):
        self.nexts = defaultdict(TrieNode)
        self.isword = False


class Trie:

    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            self.insert(w[::-1])

    def insert(self, w):
        cur = self.root
        for c in w:
            cur = cur.nexts[c]
        cur.isword = True

    def search(self, w):
        cur = self.root
        for i in range(len(w) - 1, -1, -1):
            if w[i] in cur.nexts:
                cur = cur.nexts[w[i]]
                if cur.isword:
                    return True
            else:
                return False
        return cur.isword


class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = Trie(words)
        self.cache = list()

    def query(self, letter: str) -> bool:
        self.cache.append(letter)
        return self.t.search(self.cache)
