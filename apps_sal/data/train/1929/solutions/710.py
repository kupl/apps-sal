class StreamChecker:

    def __init__(self, words: List[str]):
        def Trie(): return collections.defaultdict(Trie)
        self.trie = Trie()

        for word in words:
            functools.reduce(dict.__getitem__, word, self.trie)['

        self.heads = []

    def query(self, letter: str) -> bool:
        self.heads = [h[letter] for h in self.heads if letter in h]
        if letter in self.trie:
            self.heads.append(self.trie[letter])
        return any('
