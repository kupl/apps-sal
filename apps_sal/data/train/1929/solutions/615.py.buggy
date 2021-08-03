class StreamChecker:

    def __init__(self, words: List[str]):
        self.tracker=\"\"
        self.map={}
        
        for word in words:
            curr=self.map
            for letter in word[::-1]:
                if letter not in curr:
                    curr[letter]={}
                curr=curr[letter]
            curr[\"$\"]={}
                
                    
                
    def query(self, letter: str) -> bool:
        
        self.tracker+=letter
        curr=self.map
        for l in self.tracker[::-1]:
            if l not in curr:
                return False
            curr=curr[l]
            
            if \"$\" in curr:
                return True
        
        return False
            
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
