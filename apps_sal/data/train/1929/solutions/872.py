class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = set(words)
        self.query_history = \"\"
        self.max_word_len = max(map(len, words))

    def query(self, letter: str) -> bool:
        self.query_history = self.query_history[-self.max_word_len + 1:] + letter
        return any(self.query_history.endswith(word) for word in self.words)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
