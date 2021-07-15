class Solution: # counters or 2 pointers
    from collections import Counter
    def findSpecialInteger(self, arr: List[int]) -> int:
        res = Counter(arr)
        ans = 0
        for key, value in list(res.items()):  
            if value / sum(res.values()) > 0.25: # 25%
                ans = key
        return ans

