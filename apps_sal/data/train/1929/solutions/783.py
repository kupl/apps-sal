class TrieNode:

    def __init__(self):
        self.children = {}
        self.char = None
        self.isEnd = False

    def contains(self, c):
        return c in self.children

    def set(self, c):
        self.children[c] = TrieNode()

    def getChild(self, c):
        return self.children[c]


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return
        word = word[::-1]
        it = self.root
        for c in word:
            if not c in it.children:
                it.children[c] = TrieNode()
                it.children[c].char = c
            it = it.children[c]
        it.isEnd = True

    def hasAnyPrefix(self, letters):
        it = self.root
        for c in letters:
            if it.isEnd:
                return True
            if not it.contains(c):
                return False
            it = it.getChild(c)
        return it.isEnd


class StreamChecker:

    def __init__(self, words: List[str]):
        from collections import deque
        self.letters = deque([])
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)

    def query(self, letter: str) -> bool:
        self.letters.appendleft(letter)
        return self.trie.hasAnyPrefix(self.letters)
