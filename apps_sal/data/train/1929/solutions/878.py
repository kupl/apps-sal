class StreamChecker:

    def __init__(self, words: List[str]):
        self.letters = ''
        self.words = words
        self.max_length = max([len(x) for x in words])

    def query(self, letter: str) -> bool:
        self.letters += letter
        self.letters = self.letters[-self.max_length:]
        # print(letter)
        for word in self.words:
            if word[-1] != letter:
                continue
            letters_word = self.letters[-len(word):]
            # print(f'{word} == {letters_word} ??')
            if word == letters_word:
                # print(True, word)
                return True
        # print(False)
        return False



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

