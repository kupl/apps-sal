class StreamChecker:
    class TrieNode:
        def __init__(self):
            self.d = {}
            self.word = False

        def add(self, word):
            node = self
            for c in word:
                if c not in node.d:
                    node.d[c] = StreamChecker.TrieNode()
                node = node.d[c]
            node.word = True

        def __repr__(self):
            return f'{self.d}'

    def __init__(self, words: List[str]):
        t = self.TrieNode()
        for word in words:
            t.add(word)
        self.root = t
        self.tries = []

    def query(self, letter: str) -> bool:
        self.tries = [e.d[letter] for e in self.tries if letter in e.d]
        if letter in self.root.d:
            self.tries.append(self.root.d[letter])
        return any([e.word for e in self.tries])

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
