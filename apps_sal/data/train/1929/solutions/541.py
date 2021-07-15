class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.chars = \"\"
        self._last_letters = set(w[-1] for w in words)
        
    def query(self, letter: str) -> bool:
        self.chars += letter
        if letter not in self._last_letters:
            return False
        return any(self.chars.endswith(w) for w in self.words)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
