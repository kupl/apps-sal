class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_word = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = self.build(words)
        self.history = []

    def query(self, letter: str) -> bool:
        self.history.append(self.root)
        tmp = [node.children[letter] for node in self.history if letter in node.children]
        self.history = tmp
        for node in tmp:
            if node.is_word:
                return True
        return False

    def build(self, words):
        root = TrieNode()
        for word in words:
            tmp = root
            for c in word:
                if c not in tmp.children:
                    tmp.children[c] = TrieNode()
                tmp = tmp.children[c]
            tmp.is_word = True
        return root

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

