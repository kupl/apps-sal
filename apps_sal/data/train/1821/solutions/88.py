class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res, l, N = [0] * len(nums), 1, len(nums)

        def _merge(ll, lh, rl, rh):
            if rl >= N:
                for i in range(ll, N):
                    res[i] = nums[i]
            else:
                p, q, i = ll, rl, ll
                while p < lh and q < rh:
                    if nums[p] <= nums[q]:
                        res[i], p = nums[p], p + 1
                    else:
                        res[i], q = nums[q], q + 1
                    i += 1
                b, e = (p, lh) if p < lh else (q, rh)
                for j in range(b, e):
                    res[i] = nums[j]
                    i += 1

        while l < N:
            b = 0
            while b < N:
                _merge(b, b + l, b + l, min(N, b + 2 * l))
                b += 2 * l
            l, nums, res = l * 2, res, nums
        return nums
