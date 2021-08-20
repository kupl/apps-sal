import collections


class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, s):
        root = self
        for c in s:
            if root.children[ord(c) - ord('a')] is None:
                root.children[ord(c) - ord('a')] = Trie()
            root = root.children[ord(c) - ord('a')]
        root.is_end = True

    def search(self, s):
        root = self
        for c in s:
            if root.children[ord(c) - ord('a')] is None:
                return False
            root = root.children[ord(c) - ord('a')]
            if root.is_end:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        self.stream = collections.deque()
        for w in words:
            self.root.insert(reversed(w))

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.root.search(self.stream)
