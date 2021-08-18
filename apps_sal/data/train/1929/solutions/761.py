END = '_'


class StreamChecker:
    def __init__(self, words: List[str]):
        self.tree = {}
        self.queries = []

        for w in words:
            sub = self.tree
            for c in w:
                if c not in sub:
                    sub[c] = {}
                sub = sub[c]
            sub[END] = END

    def query(self, l: str) -> bool:
        found = False

        self.queries.append(self.tree)

        qs = []

        for q in self.queries:
            if l in q:
                qs.append(q[l])
                if END in q[l]:
                    found = True

        self.queries = qs

        return found
