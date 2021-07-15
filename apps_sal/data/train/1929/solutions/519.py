class StreamChecker:
    def __init__(self, words: List[str]):
        self.mDict = defaultdict(list)
        for word in words:
            self.mDict[word[-1]].append(word[:-1])
        self.currStr = \"\"
    def query(self, letter: str) -> bool:
        self.currStr += letter
        if letter in self.mDict:
            for curr in self.mDict[letter]:
                length = len(curr)+1
                if len(self.currStr) >= length and  (curr+letter) == self.currStr[-length:]:
                    return True
            return False
        else:#No word so far ending in this letter
            return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
