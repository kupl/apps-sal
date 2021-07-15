class StreamChecker:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.terminal = False
            
    def __init__(self, words: List[str]):
        self.array = []
        self.root = self.TrieNode()
        for word in words:
            node = self.root
            for char in word[::-1]:
                if char not in node.children:
                    node.children[char] = self.TrieNode()
                node = node.children[char]
            node.terminal = True

    def query(self, letter: str) -> bool:
        self.array.append(letter)
        node = self.root
        array = self.array[::-1]
        for char in array:
            if char in node.children:
                node = node.children[char]
                if node.terminal:
                    return True
            else:
                return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

