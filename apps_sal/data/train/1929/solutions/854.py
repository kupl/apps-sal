class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = {}
        for word in words:
            curr = self.t
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr[''] = None
            
        self.cursor = []
        
    def query(self, letter: str) -> bool:
        self.cursor = [x[letter] for x in self.cursor if letter in x]
        if letter in self.t:
            self.cursor.append(self.t[letter])
        for c in self.cursor:
            if '' in c:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

