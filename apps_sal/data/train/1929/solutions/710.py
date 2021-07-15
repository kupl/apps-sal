class StreamChecker:

    def __init__(self, words: List[str]):
        Trie = lambda: collections.defaultdict(Trie)
        self.trie = Trie()

        for word in words:
            functools.reduce(dict.__getitem__, word, self.trie)['#'] = True

        self.heads = []

    def query(self, letter: str) -> bool:
        self.heads = [h[letter] for h in self.heads if letter in h]
        if letter in self.trie:
            self.heads.append(self.trie[letter])
        return any('#' in h for h in self.heads)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

