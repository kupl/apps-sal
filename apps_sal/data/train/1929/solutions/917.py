class StreamChecker:

    def __init__(self, words: List[str]):
        self.context = []
        self.map = [{}, False]

        for w in words:
            it = self.map
            for c in w:
                if c not in it[0]:
                    it[0][c] = [{}, False]
                it = it[0][c]
            it[1] = True

    def query(self, letter: str) -> bool:
        new_context = []
        for m in self.context:
            if letter in m[0]:
                new_context.append(m[0][letter])

        if letter in self.map[0]:
            new_context.append(self.map[0][letter])

        self.context = new_context
        for m in self.context:
            if m[1]:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
