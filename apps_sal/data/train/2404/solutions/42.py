class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        a = [i for i in range(1, arr[-1] + k + 10)]
        return [i for i in a if i not in arr][k - 1]
