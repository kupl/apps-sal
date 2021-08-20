from collections import deque


class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.end = False

    def insert(self, S):
        t = self
        for c in S:
            if not t.children[ord(c) - ord('a')]:
                t.children[ord(c) - ord('a')] = Trie()
            t = t.children[ord(c) - ord('a')]
        t.end = True

    def search(self, stream):
        t = self
        for c in stream:
            if not t.children[ord(c) - ord('a')]:
                return False
            t = t.children[ord(c) - ord('a')]
            if t.end:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = Trie()
        self.stream = deque()
        for word in words:
            self.t.insert(reversed(word))

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.t.search(self.stream)
