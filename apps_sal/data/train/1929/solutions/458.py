class StreamChecker:

    def __init__(self, words: List[str]):
        self.tab = collections.defaultdict(set)
        for w in words:
            self.tab[w[-1]].add(w)
        self.queried = ''

    def query(self, letter: str) -> bool:
        self.queried += letter
        if letter not in self.tab:
            return False
        candidates = self.tab[letter]
        for can in candidates:
            if can == self.queried[-len(can):]:
                return True
        return False
