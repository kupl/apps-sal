class TrieNode:

    def __init__(self, end=False):
        self.end = end
        self.lnk = {}


class StreamChecker:

    def __init__(self, words: List[str]):
        self.head = TrieNode()
        for w in words:
            x = self.head
            for (i, c) in enumerate(w):
                if c not in x.lnk:
                    y = TrieNode()
                    x.lnk[c] = y
                x = x.lnk[c]
            x.end = True
        self.ptrs = []

    def query(self, letter: str) -> bool:
        self.ptrs.append(self.head)
        found = False
        new_ptrs = []
        for p in self.ptrs:
            if letter in p.lnk:
                q = p.lnk[letter]
                new_ptrs.append(q)
                found |= q.end
        self.ptrs = new_ptrs
        return found
