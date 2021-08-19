class StreamChecker:

    def __init__(self, words: List[str]):
        self.dict = {}
        self.longest = 0
        for word in words:
            if self.longest < len(word):
                self.longest = len(word)
            for i in range(len(word) - 1, 0, -1):
                if self.dict.get(len(word[i:])) == None:
                    self.dict[len(word[i:])] = {word[i:]: 0}
                elif self.dict[len(word[i:])].get(word[i:]) == None:
                    self.dict[len(word[i:])][word[i:]] = 0
            if self.dict.get(len(word)) == None:
                self.dict[len(word)] = {word: 1}
            else:
                self.dict[len(word)][word] = 1
        self.letters = ''

    def query(self, letter: str) -> bool:
        if len(self.letters) == self.longest:
            self.letters = self.letters[1:]
        self.letters += letter
        i = len(self.letters) - 1
        while i >= 0 and self.dict[len(self.letters[i:])].get(self.letters[i:]) != None:
            if self.dict[len(self.letters[i:])][self.letters[i:]] == 1:
                return True
            i -= 1
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
