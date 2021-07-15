class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        res = set()
        res.add(stones[0])
        for n in stones[1:]:
            newres = set()
            for m in res:
                newres.add(n + m)
                newres.add(abs(n - m))
            res = newres
        return min(res)
