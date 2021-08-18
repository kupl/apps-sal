class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            ptr = self.trie
            for ch in word:
                if ch not in ptr:
                    ptr[ch] = {}
                ptr = ptr[ch]
            ptr[None] = {}

        self.ptrs = []

    def query(self, letter: str) -> bool:
        ptrs = []
        ret = False
        for ptr in self.ptrs:
            if letter in ptr:
                ptrs.append(ptr[letter])
                ret |= None in ptr[letter]

        if letter in self.trie:
            ptrs.append(self.trie[letter])
            ret |= None in self.trie[letter]

        self.ptrs = ptrs
        return ret
