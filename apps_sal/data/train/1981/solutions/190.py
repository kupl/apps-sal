class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        start_end_count = [[0, 0] for _ in nums]
        for start, end in requests:
            start_end_count[start][0] += 1
            start_end_count[end][1] += 1
        counts = [0 for _ in nums]
        count = 0
        for i, (sc, ec) in enumerate(start_end_count):
            count += sc
            counts[i] = count
            count -= ec
        return sum([a * b % 1000000007 for a, b in zip(sorted(counts), sorted(nums))]) % 1000000007
