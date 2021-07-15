class StreamChecker:
    
    def __init__(self, words: List[str]):
        self.d = {}
        self.queries = \"\"
        for word in words:
            self.d.setdefault(word[-1],set())
            self.d[word[-1]].add(word[:-1])
        

    def query(self, letter: str) -> bool:
        self.queries += letter
        if letter not in self.d: return False
        for word in self.d[letter]:
            if(len(self.queries)>=len(word)+1)and((word+letter) == self.queries[-(len(word)+1):]): return True
        return False
                
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
