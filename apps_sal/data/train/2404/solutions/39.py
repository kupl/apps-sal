class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = max(arr) + k
        com = [i for i in range(1, l + 1) if i not in arr]
        return com[k - 1]
