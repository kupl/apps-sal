class StreamChecker:

    def __init__(self, words: List[str]):
        self.history = \"\"
        self.li = {}
        
        for word in words:
            curr = self.li
            for c in word[::-1]:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            
            curr[\"#\"] = {}

    def query(self, letter: str) -> bool:
        self.history += letter
        
        curr = self.li
        for l in self.history[::-1]:
            if l not in curr:
                return False
            
            if \"#\" in curr[l]:
                return True
            
            curr = curr[l]
        
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
