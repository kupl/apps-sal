class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            cur = self.trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur[\"-\"] = True
        self.currents = [self.trie]

    def query(self, letter: str) -> bool:
        keep = [self.trie]
        found = False
        for v in self.currents:
            if letter in v:
                vv = v[letter]
                found |= \"-\" in vv
                if \"-\" not in vv or len(vv) > 1:
                    keep.append(vv)

        self.currents = keep
        return found

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
