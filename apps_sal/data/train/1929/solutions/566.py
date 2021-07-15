class StreamChecker:

    def __init__(self, words: List[str]):
        self.dict = {}
        for word in words:
            if word[-1] not in self.dict:
                self.dict[word[-1]] = [word[:-1]]
            else:
                self.dict[word[-1]].append(word[:-1])
        
        self.s = \"\"
        
    def query(self, letter: str) -> bool:
        self.s += letter
        if letter in self.dict:
            for word in self.dict[letter]:
                length = len(word) + 1
                cword = word + letter
                if len(self.s) >= length and cword == self.s[-length:]:
                    return 1
            return 0
        else:
            return 0
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
