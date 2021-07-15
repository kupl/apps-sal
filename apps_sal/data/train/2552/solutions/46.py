from collections import defaultdict

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        for i in arr:
            counts[i] += 1
        return max(counts.items(), key=lambda x : x[1])[0]
