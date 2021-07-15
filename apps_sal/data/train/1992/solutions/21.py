class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combo = []
        self.find_combo(0, combinationLength, characters, \"\")
        self.combo.sort()
        self.pos = -1
        
        

    def next(self) -> str:
        self.pos += 1
        
        return self.combo[self.pos]
        
        
    def hasNext(self) -> bool:
        return self.pos + 1 < len(self.combo)
    
    def find_combo(self, idx, end, characters, cur):
        if idx == len(characters):
            if len(cur) == end:
                self.combo.append(cur[:])
        
        else:
            self.find_combo(idx + 1, end, characters, cur + characters[idx])
            self.find_combo(idx + 1, end, characters, cur)
            
            
        
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
