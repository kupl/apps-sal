class Trie:

    def __init__(self):
        self.endOfWord = False
        self.children = [None] * 26

    def insert(self, s):
        t = self
        for c in s:
            if t.children[ord(c) - ord('a')] == None:
                t.children[ord(c) - ord('a')] = Trie()
            t = t.children[ord(c) - ord('a')]
        t.endOfWord = True

    def search(self, s):
        t = self
        for c in s:
            if t.children[ord(c) - ord('a')] == None:
                return False
            t = t.children[ord(c) - ord('a')]
            if t.endOfWord:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = Trie()
        self.stream = collections.deque()
        for w in words:
            self.t.insert(reversed(w))

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.t.search(self.stream)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
