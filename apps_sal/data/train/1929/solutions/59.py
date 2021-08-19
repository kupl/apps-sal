class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.points = [self.trie]
        for word in words:
            cur = self.trie
            for w in word:
                if not w in cur:
                    cur[w] = {}
                cur = cur[w]
            cur['#'] = None

    def query(self, letter: str) -> bool:
        temp = [self.trie]
        ret = False
        for p in self.points:
            if letter in p:
                p = p[letter]
                if '#' in p:
                    ret = True
                temp.append(p)
        self.points = temp
        return ret
