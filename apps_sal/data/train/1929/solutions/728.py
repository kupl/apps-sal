class StreamChecker:

    def __init__(self, words: List[str]):

        def T():
            return collections.defaultdict(T)
        self.trie = T()
        for w in words:
            functools.reduce(dict.__getitem__, w, self.trie)['#'] = True
        self.possible_list = []

    def query(self, letter: str) -> bool:
        self.possible_list = [node[letter] for node in self.possible_list + [self.trie] if letter in node]
        return any(('#' in node for node in self.possible_list))
