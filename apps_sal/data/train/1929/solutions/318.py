class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.history = []
        for word in words:
            node = self.root
            for char in word[::-1]:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.terminal = True

    def query(self, letter: str) -> bool:
        self.history.append(letter)
        node = self.root
        for i in reversed(list(range(len(self.history)))):
            if self.history[i] in node.children:
                node = node.children[self.history[i]]
                if node.terminal:
                    return True
            else:
                return False
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
