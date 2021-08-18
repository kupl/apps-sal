class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        m, n = len(requests), len(nums)
        ind_count = dict()
        start_count = dict()
        end_count = dict()
        for s, e in requests:
            start_count[s] = start_count.get(s, 0) + 1
            end_count[e + 1] = end_count.get(e + 1, 0) + 1
        count = 0
        for ind in range(n):
            count = count + start_count.get(ind, 0) - end_count.get(ind, 0)
            if count > 0:
                ind_count[ind] = count

        inds = sorted(list(ind_count.keys()), key=lambda k: ind_count[k], reverse=True)
        nums = sorted(nums, reverse=True)
        out = 0
        for i, ind in enumerate(inds):
            out += ind_count[ind] * nums[i]
        return out % (10**9 + 7)
