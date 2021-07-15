class StreamChecker:
    def __init__(self, words):
        self.buffer = \"\"
        self.tree = {}
        self.null = '\\0'
        for w in words:
            self.insert(w[::-1])


    def query(self, letter):
        self.buffer = letter + self.buffer
        curr = self.tree
        for c in self.buffer:
            if c in curr:
                curr = curr[c]
                if self.null in curr:
                    return True
            else:
                break
        return False

    def insert(self, word: str) -> None:
        \"\"\"
        Inserts a word into the trie.
        \"\"\"
        tree = self.tree
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        tree[self.null] = {}


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
