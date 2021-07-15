class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:

    
        n = {}
        def find(x):
            n[x] = find(n[x] + 1) if x in n else x
            return n[x]
        return sum(find(a) - a for a in A)
