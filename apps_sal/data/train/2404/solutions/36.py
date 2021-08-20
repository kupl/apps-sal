class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        for num in range(1, len(arr) + k + 1):
            if num not in arr:
                missing.append(num)
        return missing[k - 1]
