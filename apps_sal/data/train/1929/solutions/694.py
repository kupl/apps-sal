class StreamChecker():
    def __init__(self, words: List[str]):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w, self.trie)['#'] = True
        self.waiting = []

    def query(self, letter: str) -> bool:
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any(\"#\" in node for node in self.waiting)
