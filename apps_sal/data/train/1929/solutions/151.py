class Trie:
    def __init__(self):
        self.prev = {}


class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = Trie()
        self.maxlens = 0
        self.backw = ''
        for w in words:
            wn = len(w)
            if wn > self.maxlens:
                self.maxlens = wn
            wt = self.t
            for i in range(wn - 1, -1, -1):
                if w[i] not in wt.prev:
                    wt.prev[w[i]] = Trie()
                wt = wt.prev[w[i]]
            wt.prev['$'] = '$'

    def query(self, letter: str) -> bool:
        if len(self.backw) == self.maxlens:
            self.backw = self.backw[1:]
        self.backw += letter
        wn = len(self.backw)
        wt = self.t
        for i in range(wn - 1, -1, -1):
            if self.backw[i] not in wt.prev:
                return False
            wt = wt.prev[self.backw[i]]
            if '$' in wt.prev:
                return True
        return '$' in wt.prev


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
