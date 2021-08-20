class Node:

    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False


class WordTree:

    def __init__(self):
        self.root = Node(0)

    def add_word(self, word):
        cur = self.root
        for c in word[::-1]:
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = Node(c)
                cur = cur.children[c]
        cur.end = True


class StreamChecker:

    def __init__(self, words):
        self.tree = WordTree()
        for word in words:
            self.tree.add_word(word)
        self.query_l = []

    def query(self, letter: str) -> bool:
        self.query_l.append(letter)
        cur = self.tree.root
        for c in self.query_l[::-1]:
            if c not in cur.children:
                return False
            cur = cur.children[c]
            if cur.end:
                return True
        return False
