class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = {}
        for w in words:
            if len(w) not in list(self.words.keys()):
                self.words[len(w)] = []
            self.words[len(w)].append(w)
        self.buffer = ''
        self.i = 0
        self.max = max(list(self.words.keys()))
        self.res = {}

    def query(self, letter: str) -> bool:
        self.buffer += letter
        if len(self.buffer) > self.max:
            self.buffer = self.buffer[-self.max:]
        if self.buffer in list(self.res.keys()):
            return self.res[self.buffer]
        if len(self.buffer) not in list(self.words.keys()):
            return False
        for i in self.words:
            if len(self.buffer) >= i and self.buffer[-i:] in self.words[i]:
                self.res[self.buffer] = True
                return True
        self.res[self.buffer] = False
        return False
