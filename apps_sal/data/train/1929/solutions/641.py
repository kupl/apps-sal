class StreamChecker:

    def __init__(self, words: List[str]):

        def T():
            return collections.defaultdict(T)
        self.trie = T()
        self.waiting = []
        for w in words:
            d = self.trie
            for c in w:
                d = d[c]
            d = d['#']

    def query(self, letter: str) -> bool:
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any((d for d in self.waiting if '#' in d))
