class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        indmap = {ind: 0 for ind in range(len(nums))}
        for r in requests:
            indmap[r[0]] += 1
            if r[1] + 1 < len(nums):
                indmap[r[1] + 1] -= 1
        for i in range(1, len(nums)):
            indmap[i] += indmap[i - 1]
        indices_sorted_by_occ = sorted(indmap.keys(), key=lambda ind: indmap[ind], reverse=True)
        sorted_freqs = [indmap[ind] for ind in indices_sorted_by_occ]
        sorted_nums = sorted(nums, reverse=True)
        sol = sum((n * f for (n, f) in zip(sorted_nums, sorted_freqs)))
        return sol % (10 ** 9 + 7)
