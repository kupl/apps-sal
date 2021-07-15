from collections import defaultdict
def routing():
    return defaultdict(routing)
class StreamChecker:
    def __init__(self, words: List[str]):
        self.router = routing()
        for word in words:
            root = self.router
            for letter in word:
                root = root[letter]
            root[\"*\"] = word
        self.queries = []
    def query(self, letter: str) -> bool:
        new_queries, matches = [], []
        self.queries.append(self.router)
        for q in self.queries:
            if letter in q:
                q = q[letter]
                if '*' in q:
                    matches.append(q[\"*\"])
                    if len(q) > 1:
                        new_queries.append(q)
                else:
                    new_queries.append(q)
        self.queries = new_queries
        return bool(matches)
