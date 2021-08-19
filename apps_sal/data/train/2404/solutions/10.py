class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        real = list(range(1, arr[-1] + k + 1))
        missing = sorted(list(set(real) - set(arr)))
        return missing[k - 1]
