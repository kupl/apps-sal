class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            trie = self.trie
            for letter in word:
                trie = trie.setdefault(letter, {})
            trie[' '] = {}
        self.check = []

    def query(self, letter: str) -> bool:
        self.check.append(self.trie)
        self.check = [trie[letter] for trie in self.check if letter in trie]
        for trie in self.check:
            if ' ' in trie:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
