class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for w in words:
            t = self.trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['
        self.poss = []

    def query(self, letter: str) -> bool:

        waitlist = []

        if letter in self.trie:
            waitlist.append(self.trie[letter])

        for t in self.poss:
            if letter in t:
                waitlist.append(t[letter])
        self.poss = waitlist
        return any('
