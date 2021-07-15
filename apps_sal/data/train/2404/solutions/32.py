class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = 0
        for i in list(range(1, arr[-1]+k+1)):
            if i not in arr:
                n += 1
                if k == n:
                    return i
