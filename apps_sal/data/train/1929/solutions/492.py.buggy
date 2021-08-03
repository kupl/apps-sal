class StreamChecker:

    def __init__(self, words: List[str]):
        self.cache = dict()
        for word in words:
            if word[-1] not in self.cache:
                self.cache[word[-1]] = [word[:-1]]
            else:
                self.cache[word[-1]].append(word[:-1])
        
        self.string = \"\"

    def query(self, letter: str) -> bool:
        self.string += letter
        if letter in self.cache:
            for word in self.cache[letter]:
                length = len(word) + 1
                complete_word = word + letter
                if len(self.string) >= length and complete_word == self.string[- length:]:
                    return True
            return False
        else:
            return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
