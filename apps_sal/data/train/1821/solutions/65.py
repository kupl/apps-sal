class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        count = [0] * 100010
        for n in nums:
            count[n + 50000] += 1
        res = []
        for c in range(100010):
            while count[c] > 0:
                res.append(c - 50000)
                count[c] -= 1
        return res
