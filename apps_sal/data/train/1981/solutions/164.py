class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        from queue import PriorityQueue
        from collections import defaultdict
        q = PriorityQueue()

        sorted_nums = sorted(nums)

        dig_dict = defaultdict(int)
        for r in requests:
            dig_dict[r[0]] += 1
            dig_dict[r[1] + 1] -= 1

        for i in range(1, len(nums) + 1):
            dig_dict[i] += dig_dict[i - 1]

        for k, v in list(dig_dict.items()):
            q.put((-v, k))

        final_pos = {}
        pointer = len(nums) - 1
        res = 0
        while q.qsize() > 0:
            # final_post[q.get()[1]] = sorted_nums[pointer]
            res += q.get()[0] * -1 * sorted_nums[pointer]
            pointer -= 1

        return res % (10**9 + 7)
