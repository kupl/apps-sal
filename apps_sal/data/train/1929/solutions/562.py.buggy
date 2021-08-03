class StreamChecker:

    def __init__(self, words: List[str]):
        self.d = {}
        for word in words:
            if not word[-1] in self.d:
                self.d[word[-1]] = [word[:-1]]
            else:
                self.d[word[-1]].append(word[:-1])
        
        self.string = \"\"

    def query(self, letter: str) -> bool:
        self.string += letter
        if letter in self.d:
            for word in self.d[letter]:
                length = len(word) + 1
                complete_word = word + letter
                if len(self.string) >= length and complete_word == self.string[-length:]:
                    return True
            return False
        else:
            return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
