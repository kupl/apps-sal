class StreamChecker:

    def __init__(self, words: List[str]):
        
        
        self.q = []
        
        self.head = {}
        for word in words:
            cur = self.head
            for w in word[::-1]:
                if w not in cur:
                    cur[w] = {}
                
                cur = cur[w]
            
            cur[\"$\"] = True 
        
        

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        
        cur = self.head
        for c in self.q[::-1]:
            if \"$\" in cur:
                return True
            
            if c not in cur:
                return False
            
            cur = cur[c]
            
        
        return '$' in cur


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
