class StreamChecker:

    def __init__(self, words: List[str]):
        from collections import defaultdict
        self.word = sorted(words, key = lambda x: (x[-1], len(x)))
        self.lett = \"\"
        self.d = defaultdict(str)
        for i in range(1, len(self.word) + 1):
            if not self.d[self.word[i - 1][-1]]:
                self.d[self.word[i - 1][-1]] = i   
                

    def query(self, letter: str) -> bool:
        self.lett += letter
        if not letter in self.d:
            return False
        begin = self.d[letter] - 1       
        
        for i in self.word[begin:]:
            if len(self.lett) < len(i):
                return False
            if i[-1] != letter:
                return False
            if self.lett[-len(i):] == i:
                return True
        return False
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
