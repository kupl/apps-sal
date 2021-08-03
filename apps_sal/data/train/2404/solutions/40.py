class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        n = arr[-1]
        x = 0
        count = 0

        for i in range(1, n + 1 + k):
            if i not in arr:
                count += 1
                if count == k:
                    x = i

        return x
