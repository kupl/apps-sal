class TrieNode:
    def __init__(self):
        self.isword = False
        self.children = [None] * 26


class StreamChecker:

    def __init__(self, words):
        self.root = TrieNode()
        self.lastchars = []
        for word in words:
            self.add(word)

    def add(self, word):
        parent = self.root
        for c in reversed(word):
            i = ord(c) - 97
            if not parent.children[i]:
                parent.children[i] = TrieNode()
            parent = parent.children[i]
        parent.isword = True

    def search(self, word):
        parent = self.root

        for c in reversed(word):
            i = ord(c) - 97
            if parent.isword:
                return True
            if not parent.children[i]:
                return False
            parent = parent.children[i]

        return parent.isword

    def query(self, letter):
        self.lastchars.append(letter)
        return self.search(self.lastchars)
