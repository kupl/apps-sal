class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        rng = [0] * (n + 1)
        for req in requests:
            l, r = req
            rng[l], rng[r + 1] = rng[l] + 1, rng[r + 1] - 1
        lst = []
        for i in range(n):
            if i:
                rng[i] += rng[i - 1]
            lst.append(rng[i])

        ans = 0
        return sum(num * cnt for num, cnt in zip(sorted(nums, reverse=True), sorted(lst, reverse=True))) % 1000000007
