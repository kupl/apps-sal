class StreamChecker:
    def __init__(self, words: List[str]):
        nested = lambda: defaultdict(nested)
        self.root = nested()

        for w in words:
            n = self.root
            for c in w:
                n = n[c]
            n[\"\\0\"] = True
        self.partials = [self.root]

    def query(self, letter: str) -> bool:
        self.partials = [self.root] + [p[letter] for p in self.partials if p[letter]]

        return any(\"\\0\" in p for p in self.partials)

