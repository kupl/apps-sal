arr = [2, 3, 4, 7, 11]
k = 5


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        return [x for x in range(1, len(arr) + k + 1) if x not in arr][k - 1]


solution = Solution()
solution.findKthPositive(arr, k)
