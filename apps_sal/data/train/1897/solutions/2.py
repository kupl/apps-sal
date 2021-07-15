class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        
        prefix = []
        curr = 0
        for n in arr:
            curr ^= n
            prefix.append(curr)
            
        res = []
        for l, r in queries:
            if l == 0:
                res.append(prefix[r])
            else:
                res.append(prefix[r] ^ prefix[l-1])
        return res
