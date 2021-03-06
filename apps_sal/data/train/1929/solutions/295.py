class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = ''
        self.dict = collections.defaultdict(set)
        for word in words:
            self.dict[word[-1]].add(word)

    def query(self, letter: str) -> bool:
        self.s += letter
        return any((self.s.endswith(word) for word in self.dict[letter]))
