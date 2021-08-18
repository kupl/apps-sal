class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = set(words)
        self.hist = ''

    def query(self, letter: str) -> bool:
        self.hist += letter
        for word in self.words:
            if self.hist[-len(word):] == word:
                return True

        return False
