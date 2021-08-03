class StreamChecker:

    def __init__(self, words: List[str]):
        # construct a trie (a dict of dicts)
        self.root = {}
        for word in words:
            sub = self.root
            for c in word:
                sub = sub.setdefault(c, {})
            sub['0'] = None
        self.current = []

    def query(self, letter: str) -> bool:
        newQueries = []
        checker = False
        for query in self.current:
            if letter in query:
                nextQuery = query[letter]
                checker = checker or '0' in nextQuery
                newQueries.append(nextQuery)
        if letter in self.root:
            nextQuery = self.root[letter]
            checker = checker or '0' in nextQuery
            newQueries.append(nextQuery)
        self.current = newQueries
        return checker


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
