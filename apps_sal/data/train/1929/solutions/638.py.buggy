class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = list(set(words))
        self.chars = \"\"
        self._single_letters = set(w for w in words if len(w) == 1)
        self._last_letters = set(w[-1] for w in words)
        self._last_pairs = set(w[-2:] for w in words)
        
    def query(self, letter: str) -> bool:
        self.chars += letter
        if letter not in self._last_letters:
            return False
        if letter in self._single_letters:
            return True
        if self.chars[-2:] not in self._last_pairs:
            return False
        return any(self.chars.endswith(w) for w in self.words)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
