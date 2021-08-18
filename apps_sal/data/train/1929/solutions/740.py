class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            t = self.trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['$'] = {}
        self.ptrs = deque()
        self.ptrs.append(self.trie)
        return

    def query(self, letter: str) -> bool:
        ret = False
        nextPtrs = deque()
        nextPtrs.append(self.trie)
        for ptr in self.ptrs:
            if letter in ptr:
                nextPtrs.append(ptr[letter])
                if '$' in ptr[letter]:
                    ret = True
        self.ptrs = nextPtrs
        return ret
