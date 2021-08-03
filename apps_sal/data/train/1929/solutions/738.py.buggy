class StreamChecker:

    def __init__(self, words: List[str]):
        self.tree = {}
        for word in words:
            ptr = self.tree
            for c in word:
                if c not in ptr:
                    ptr[c] = {}
                ptr = ptr[c]
            ptr[\"$\"] = word
        self.possible = []
        

    def query(self, letter: str) -> bool:
        # check if 
        nxt = []
        
        for p in self.possible:
            if letter in p:
                nxt.append(p[letter])
                
        if letter in self.tree:
            nxt.append(self.tree[letter])
                
        self.possible = nxt.copy()
        for p in self.possible:
            if \"$\" in p:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
