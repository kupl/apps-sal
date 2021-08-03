class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        res = []

        for i in range(1, arr[-1]):
            if i not in arr:
                res.append(i)

        if len(res) == 0 or len(res) < k:
            return arr[-1] + k - len(res)
        else:
            return res[k - 1]
