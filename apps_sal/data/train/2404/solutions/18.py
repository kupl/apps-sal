class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(1, arr[-1]):
            if i not in arr:
                k -= 1
                if not k:
                    return i
        return arr[-1] + k
