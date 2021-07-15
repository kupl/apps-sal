class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        
        def count(s):
            res = [0]*26
            for x in s:
                res[ord(x)-ord('a')] += 1
            return res
        
        bmax = [0]*26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)
        
        res = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                res.append(a)
        return res
