class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_child(self, c):
        return self.children.setdefault(c, TrieNode())

    def get_child(self, c):
        return self.children.get(c)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.data = []
        self.root = TrieNode()
        for word in words:
            node = self.root
            for c in reversed(word):
                node = node.add_child(c)
            node.is_word = True

    def query(self, letter: str) -> bool:
        self.data.append(letter)
        node = self.root
        for i in range(len(self.data) - 1, -1, -1):
            node = node.get_child(self.data[i])
            if node is not None and node.is_word:
                return True
            elif node is None:
                return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
