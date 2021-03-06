class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = set(words)
        self.letters = ''

    def query(self, letter: str) -> bool:
        self.letters += letter
        for x in self.words:
            if self.letters.endswith(x):
                return True
        return False
