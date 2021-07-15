class StreamChecker:

    def __init__(self, words: List[str]):
        self.word_set = set(words)
        self.last_letter_set = set()
        self.max_len = 0
        self.min_len = math.inf
        for w in words:
            self.last_letter_set.add(w[-1])
            if len(w) > self.max_len:
                self.max_len = len(w)
            if len(w) < self.min_len:
                self.min_len = len(w)
        self.s = \"\"

    def query(self, letter: str) -> bool:
        self.s += letter
        if letter in self.last_letter_set:
            for i in range(max(len(self.s)-self.max_len, 0), len(self.s)-self.min_len+1):
                if self.s[i:] in self.word_set:
                    return True
        return False
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
