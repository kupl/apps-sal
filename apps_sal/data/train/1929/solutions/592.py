class TrieNode:

    def __init__(self):
        self.nodes = dict()
        self.is_leaf = False

    def insert(self, word):
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def check(self, word):
        curr = self
        for c in word:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
            if curr.is_leaf:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            self.root.insert(word[::-1])
        self.sb = ''

    def query(self, letter: str) -> bool:
        self.sb += letter
        node = self.root
        return node.check(self.sb[::-1])
