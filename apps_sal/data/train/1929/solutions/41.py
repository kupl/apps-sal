class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = {}
        for w in words:
            curr = self.root
            for ch in w:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]

            curr[0] = None

        self.cursors = []

    def query(self, letter: str) -> bool:
        self.cursors.append(self.root)
        new_cursors = []
        res = False

        for c in self.cursors:
            if letter in c:
                if 0 in c[letter]:
                    res = True
                new_cursors.append(c[letter])

        self.cursors = new_cursors
        return res
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

