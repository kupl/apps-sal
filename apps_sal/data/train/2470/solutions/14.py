class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        collection = defaultdict(int)
        count = 0
        for i in dominoes:
            pair = frozenset(i)
            count+=collection[pair]
            collection[pair]+=1
                
        
        return count
