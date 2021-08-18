class Trie:
    def __init__(self, words: List[str]):
        self.trie = lambda: collections.defaultdict(self.trie)
        self.root = self.trie()

        for w in words:
            self.add(w[::-1])

    def add(self, s: str):
        curr = self.root
        for c in s:
            curr = curr[c]
        curr['

    def find(self, s: List[str]):
        curr = self.root
        for i in range(len(s) - 1, -1, -1):
            val = s[i]

            if '
                return True
            elif val in curr:
                curr = curr[val]
            else:
                return False

        return '



class StreamChecker:

    def __init__(self, words: List[str]):
        self.queries = []
        self.trie = Trie(words)

    def query(self, letter: str) -> bool:
        self.queries.append(letter)
        return self.trie.find(self.queries)
