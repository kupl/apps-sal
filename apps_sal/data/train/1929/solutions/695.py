class StreamChecker:
    def __init__(self, words: List[str]):
        def Trie(): return collections.defaultdict(Trie)
        self.trie = Trie()
        for word in words:
            reduce(dict.__getitem__, word, self.trie)['eow'] = True
        self.trie_list = []

    def query(self, letter: str) -> bool:
        self.trie_list = [node[letter] for node in self.trie_list + [self.trie] if letter in node]
        return any('eow' in trie for trie in self.trie_list)
