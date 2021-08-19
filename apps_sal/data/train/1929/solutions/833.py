class Node:

    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = Node()

    def add(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.isWord = True

    def check(self, word):
        cur = self.root
        for ch in word:
            if cur.isWord:
                return True
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.isWord


class StreamChecker:

    def __init__(self, words: List[str]):
        self.T = Trie()
        for word in words:
            self.T.add(word[::-1])
        self.arr = []

    def query(self, letter: str) -> bool:
        self.arr.append(letter)
        return self.T.check(self.arr[::-1])
