class Node:
    def __init__(self):
        self.m = {}
        self.end = False

    def get(self, c):
        return self.m.get(c)

    def put(self, c, node):
        self.m[c] = node


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for c in word[::-1]:
            if not node.get(c):
                node.put(c, Node())
            node = node.get(c)
        node.end = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = deque([])
        for word in words:
            self.trie.insert(word)

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie.root
        ans = ''
        for c in self.stream:
            if node.end:
                return True
            if not node.get(c):
                return False
            node = node.get(c)
        return node.end


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
