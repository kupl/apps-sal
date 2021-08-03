class trie:
    def __init__(self):
        self.endofword = False
        self.children = [None] * 26

    def insert(self, s):
        t = self
        for i in s:
            if t.children[ord(i) - ord('a')] == None:
                t.children[ord(i) - ord('a')] = trie()
            t = t.children[ord(i) - ord('a')]
        t.endofword = True

    def search(self, w):
        t = self
        for i in w:
            if t.children[ord(i) - ord('a')] == None:
                return False
            t = t.children[ord(i) - ord('a')]
            if t.endofword:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = trie()
        self.dequeue = []
        for i in words:
            self.t.insert(reversed(i))

    def query(self, letter: str) -> bool:
        self.dequeue.insert(0, letter)
        return self.t.search(self.dequeue)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
