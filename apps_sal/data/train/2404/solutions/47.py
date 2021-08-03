class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m = arr[-1]
        s = {}
        for i in range(m + k + 1):
            if i not in arr:
                s[i] = 1
        return list(s.keys())[k]
