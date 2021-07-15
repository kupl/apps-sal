from typing import List

class Solution:
    
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        sorted_arrs = sorted(arr)
        n = len(arr)
        median = sorted_arrs[(n - 1) // 2]
        vals = [(abs(val - median), val) for val in arr]
        vals.sort()
        return [val for comp, val in vals[-k:]]
