class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = [i ^ (i >> 1) for i in range(1 << n)]
        
        idx = res.index(start)
        return res[idx:] + res[:idx]
