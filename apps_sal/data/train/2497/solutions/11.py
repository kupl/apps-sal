class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any(arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0 for i in range(len(arr) - 2))
