class StreamChecker:

    def __init__(self, words: List[str]):
        newwords = []
        for w in words:
            if w not in newwords:
                newwords.append(w)
        self.words = newwords
        print(\"number of words = \" + str(len(self.words)))
        self.check = \"\"



    def query(self, letter: str) -> bool:
        self.check += letter
        for word in self.words:
            if word[-1] != letter:
                continue
            if len(word) > len(self.check):
                continue

            if word == self.check[-1 * len(word):]:
                return True
        return False
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
