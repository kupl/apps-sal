class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, w):
        t = self.trie
        for c in w + '\\0':
            if c not in t:
                t[c] = {}
            t = t[c]

    def match(self, w):
        t = self.trie
        for c in w:
            if c not in t:
                return False
            t = t[c]
            if '\\0' in t:
                return True


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.stream = deque()

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.trie.match(self.stream)
