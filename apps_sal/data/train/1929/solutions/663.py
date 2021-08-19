class Node(object):

    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Node()
        for word in words:
            self.root.add(word[::-1])
        self.s = []
        self.cur = self.root

    def query(self, letter: str) -> bool:
        self.s.append(letter)
        i = len(self.s) - 1
        cur = self.root
        while i >= 0:
            c = self.s[i]
            if c not in cur.children:
                return False
            cur = cur.children[c]
            if cur.end:
                return True
            i -= 1
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
