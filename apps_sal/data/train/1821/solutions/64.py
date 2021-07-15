class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        buckets = [0] * 100002
        res = []
        for i in nums:
            buckets[i + 50000] += 1
        for i in range(len(buckets)):
            if buckets[i] != 0:
                for _ in range(buckets[i]):
                    res.append(i - 50000)
        return res
