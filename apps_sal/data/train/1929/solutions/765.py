class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = list(set(words))
        self.n = max(map(len, words))
        self.historic = \"\"

    def query(self, letter: str) -> bool:
        self.historic = self.historic + letter
        if len(self.historic)>self.n:
            self.historic = self.historic[1:]
        for w in self.words:
            if self.historic[-len(w):] == w:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
