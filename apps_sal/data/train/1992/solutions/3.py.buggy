class CombinationIterator:

    def __init__(self, arr: str, l: int):
        self.result = []
        self.idx = 0
        n = len(arr)
        
        self.backtrack(arr, 0, l, n, \"\")
                        
    def backtrack(self, arr, left, ln, n, currStr):
        if ln == 0:
            self.result.append(\"\".join(sorted(currStr)))
            return
        
        for i in range(left, n):
            
            newStr = currStr
            newStr += arr[i]
            
            self.backtrack(arr, i+1, ln-1, n, newStr)
        

    def next(self) -> str:
        res = self.result[self.idx]
        self.idx += 1
        return res
        

    def hasNext(self) -> bool:
        if self.idx >= len(self.result):
            return False
        
        return True


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
