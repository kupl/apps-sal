class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        self.characters = characters
        self.combinationLength = combinationLength
        
    
        def backtrack(characters,res,cur,index):
            if len(cur) == combinationLength:
                #print(cur)
                res.append(\"\".join(cur[:]))
                return
            for i in range(index,len(self.characters)):
                cur.append(self.characters[i])
                #print(cur)
                backtrack(characters,res,cur,i+1)
                cur.pop()
        
        backtrack(characters,self.combinations,[],0)
        self.combinationsQueue = deque(self.combinations)
        print(self.combinationsQueue)
    def next(self) -> str:
        if self.combinationsQueue:
            return self.combinationsQueue.popleft()

    def hasNext(self) -> bool:
        return len(self.combinationsQueue) > 0
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
