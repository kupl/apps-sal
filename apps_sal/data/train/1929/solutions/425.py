class TrieNode:

    def __init__(self):
        self.is_leaf = False
        self.mp = {}


class StreamChecker:

    def __init__(self, words: List[str]):
        def insert(root, w):
            for c in w:
                if c not in root.mp:
                    root.mp[c] = TrieNode()
                root = root.mp[c]
            root.is_leaf = True
        self.root = TrieNode()
        for w in words:
            insert(self.root, w[::-1])
        self.s = ''

    def query(self, letter: str) -> bool:
        def find(root, s):
            for c in s[::-1]:
                if c not in root.mp:
                    return False
                root = root.mp[c]
                if root.is_leaf:
                    return True
            return False
        self.s += letter
        return find(self.root, self.s)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
