from collections import deque


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_leaf = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for c in word:
            root = root.children.setdefault(c, TrieNode())
        root.is_leaf = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = deque()
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        curr = self.trie.root
        for c in self.stream:
            if c in curr.children:
                curr = curr.children[c]
                if curr.is_leaf:
                    return True
            else:
                return False
