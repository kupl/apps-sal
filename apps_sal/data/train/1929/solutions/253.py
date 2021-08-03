class Trie:
    def __init__(self):
        self.children = dict()
        self.isend = False

    def insert(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isend = True

    def hasPrefix(self, stream):
        cur = self
        for ch in stream:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
            if cur.isend:
                return True
        return cur.isend


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.longest = 0
        for w in words:
            self.longest = max(self.longest, len(w))
            self.trie.insert(w[::-1])
        self.stream = deque()

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        if len(self.stream) > self.longest:
            self.stream.pop()
        return self.trie.hasPrefix(''.join(self.stream))


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
