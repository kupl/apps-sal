import queue
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.max_len = 0
        for w in words:
            if w:
                p = self.trie
                self.max_len = max(self.max_len, len(w))
                for idx in range(len(w) - 1, 0, -1):
                    ch = w[idx]
                    if not ch in p:
                        p[ch] = {}
                    p = p[ch]
                p[w[0]] = {'$':None}
        self.letters = []

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        p = self.trie
        idx = len(self.letters) - 1
        while p and idx >= max(len(self.letters) - self.max_len, 0):
            if '$' in p:
                return True
            l = self.letters[idx]
            if l in p:
                p = p[l]
            else:
                return False
            idx -= 1
        else:
            return '$' in p
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

