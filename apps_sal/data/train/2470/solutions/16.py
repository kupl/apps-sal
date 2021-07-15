class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # step 1: count the dominoes
        d = {}
        for dom in dominoes:
            p = tuple(sorted(dom))
            if p in d:
                d[p] += 1
            else:
                d[p] = 1
        # step calculate it 
        c = 0
        for n in d.values():
            s = n*(n-1)//2
            c += s
        return c            
