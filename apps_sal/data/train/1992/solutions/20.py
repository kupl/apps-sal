class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.last = None
        self.end = characters[-combinationLength:]
        self.gen = self.gen_comb(characters, 0, [], combinationLength)
    
    def gen_comb(self, char, start, buffer, length):
        if len(buffer) == length:
            yield ''.join(buffer)
            return
        
        for i in range(start, len(char)):
            yield from self.gen_comb(char, i+1, buffer+[char[i]], length)
        
    def __next__(self) -> str:
        self.last = next(self.gen)
        return self.last  

    def hasNext(self) -> bool:
        return self.last != self.end
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

