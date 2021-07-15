class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = dict()
        for i in arr:
            counts[i] = counts.get(i, 0) + 1
        
        return max(counts, key=counts.get)
