class StreamChecker:

    def __init__(self, words: List[str]):
        self.Trie = dict()
        for word in words:
            t = self.Trie
            for c in word:
                if c not in t:
                    t[c] = dict()
                t = t[c]
            t['$'] = word

        self.cache = []

    def query(self, letter: str) -> bool:
        newcache = []
        ret = False
        for t in self.cache + [self.Trie]:
            if letter in t:
                newcache.append(t[letter])
                if '$' in t[letter]:
                    ret = True
        self.cache = newcache
        return ret
