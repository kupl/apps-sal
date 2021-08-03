class Trie(dict):
    word = False

    def add(self, word):
        t = self
        for c in word:
            if c not in t:
                t[c] = Trie()
            t = t[c]
        t.word = True


class StreamChecker:
    def __init__(self, words: List[str]):
        self.t = Trie()
        for w in words:
            self.t.add(w)
        self.s = []

    def query(self, c: str) -> bool:
        self.s = [t[c] for t in self.s if c in t]
        if c in self.t:
            self.s.append(self.t[c])
        return any(t.word for t in self.s)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
