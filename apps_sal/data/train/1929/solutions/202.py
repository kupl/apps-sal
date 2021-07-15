class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for c in word:
            root  = root.children.setdefault(c, TrieNode())
        root.end = True

    def search(self, word):
        root = self.root
        for c in word:
            if c not in root.children:
                return False
            root = root.children[c]
            if root.end:
                return True
        return False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.curr = \"\"
        for word in words:
            self.trie.insert(reversed(word))

    def query(self, letter: str) -> bool:
        self.curr+=letter
        if self.trie.search(reversed(self.curr)):
            return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
