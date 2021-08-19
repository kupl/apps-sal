class StreamChecker:

    def __init__(self, words: List[str]):
        self.letters = ''
        self.words = words
        self.max_length = max([len(x) for x in words])

    def query(self, letter: str) -> bool:
        self.letters += letter
        self.letters = self.letters[-self.max_length:]
        for word in self.words:
            if word[-1] != letter:
                continue
            letters_word = self.letters[-len(word):]
            if word == letters_word:
                return True
        return False
