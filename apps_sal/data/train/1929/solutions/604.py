class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = set(words)
        self.last_letters = set([word[-1] for word in words])
        self.max_length = max(map(len, self.words))
        self.history = []

    def query(self, letter: str) -> bool:
        if letter in self.words:
            return True
        self.history.append(letter)
        if letter in self.last_letters:
            word = \"\"
            for i in range(min(self.max_length, len(self.history))):
                word = self.history[-1 * i - 1] + word
                if word in self.words:
                    return True
        
        while len(self.history) > self.max_length:
            self.history.pop(0)
        
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
