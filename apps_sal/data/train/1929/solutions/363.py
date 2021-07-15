class StreamChecker:

    def __init__(self, words: List[str]):
        self.rec = collections.defaultdict(set)
        self.maxsize = float('-inf')
        self.minsize = float('inf')
        for w in words:
            self.maxsize = max(len(w), self.maxsize)
            self.minsize = min(len(w), self.minsize)
            self.rec[w[-1]].add((w,len(w)))

        self.curr = \"\"

    def query(self, letter: str) -> bool:
        
        self.curr += letter        
        for w, i in self.rec[letter]:
            if i <= len(self.curr) and self.curr[-i:] == w:
                return True            
            
        self.curr = self.curr[-self.maxsize:]
            
        return False
            
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
