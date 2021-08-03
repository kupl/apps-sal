class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = self.get_combinations(characters,combinationLength,0)        
        self.next_item=0

    def next(self) -> str:
        ans= self.combinations[self.next_item]
        self.next_item+=1
        return \"\".join(ans)

    def hasNext(self) -> bool:
        return self.next_item < len(self.combinations)

    def get_combinations(self,chars, k, start):
        ans = []
        if k == 0:
            return ans
        if k==1:
            return [[char] for char in chars[start:] ]
        count = 0
        for c in chars[start:]:
            for comb in self.get_combinations(chars, k - 1,start+count+1):
                    temp = []
                    temp.append(c)
                    temp.extend(comb)
                    ans.append(temp)
            count+=1
        return ans

            
        
        
        

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
