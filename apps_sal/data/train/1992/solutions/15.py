class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combs = list(combinations(characters, combinationLength))
        self.idx = 0
        

    def next(self) -> str:
        chars = self.combs[self.idx]
        self.idx += 1
        return \"\".join(chars)
        

    def hasNext(self) -> bool:
        return self.idx < len(self.combs)
        
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
