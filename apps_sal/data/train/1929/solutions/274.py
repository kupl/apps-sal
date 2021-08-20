import collections


class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def add_word(self, word):
        curr = self
        for c in word:
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = Trie()
            curr = curr.children[ord(c) - ord('a')]
        curr.isEnd = True

    def search(self, word):
        curr = self
        for c in word:
            if curr.children[ord(c) - ord('a')] == None:
                return False
            curr = curr.children[ord(c) - ord('a')]
            if curr.isEnd:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = collections.deque()
        for w in words:
            self.trie.add_word(w[::-1])

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.trie.search(self.stream)
