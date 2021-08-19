class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # s,e,
        # at most nlogn
        cnt = [0, 0]
        mod = 10**9 + 7
        requests.sort()
        n = len(nums)
        cnt = [0] * (n)
        for s, e in requests:
            cnt[s] += 1
            if e + 1 < n:
                cnt[e + 1] -= 1

        print(cnt)
        real_cnt = []
        for c in cnt:
            real_cnt += [c + (real_cnt[-1] if real_cnt else 0)]

        cnt = real_cnt
        cnt.sort()
        nums.sort()
        print(cnt, nums)

        res = 0
        for n, c in zip(nums, cnt):
            res += n * c
        return res % (10**9 + 7)
