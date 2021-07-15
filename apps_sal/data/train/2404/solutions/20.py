class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        for i in range(1,arr[-1]+1):
            if i not in arr:
                count += 1
            if count == k:
                return i
        return (arr[-1] - count + k)
