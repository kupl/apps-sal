class StreamChecker:

    def __init__(self, words: List[str]):
        self.tire = {}
        self.tire_reverse = {}
        self.max_size = 0
        for w in words:
            self._insert(w)
            self._insert_reverse(w[::-1])
            self.max_size = max(self.max_size, len(w))

        self.q = collections.deque([], self.max_size)
        self.curr = self.tire

    def _insert(self, word):
        curr = self.tire
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['$'] = True

    def _insert_reverse(self, word):
        curr = self.tire_reverse
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['$'] = True

    def _search(self, w):
        curr = self.tire_reverse
        for c in w:
            if c in curr:
                curr = curr[c]
                if '$' in curr:
                    return True
            else:
                return False

        return False

    def query(self, letter: str) -> bool:
        self.q.append(letter)

        if letter in self.curr:
            self.curr = self.curr[letter]
            if '$' in self.curr:
                return True
            else:
                self.curr = self.tire

        w = [c for c in self.q]
        return self._search(w[::-1])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
