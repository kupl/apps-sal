class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.len = combinationLength
        self.dic = deque([x for x in itertools.combinations(self.characters,self.len)])

    def next(self) -> str:
        x = self.dic.popleft()
        return \"\".join(x)
        
    def hasNext(self) -> bool:
        if len(self.dic) != 0:
            return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
