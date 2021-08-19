class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = max(arr) + k
        com = [i for i in range(1, l + 1)]
        diff = [x for x in com if x not in arr]
        return diff[k - 1]
