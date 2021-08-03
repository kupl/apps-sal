from fractions import gcd


def min_price(nums):
    nums.sort()
    ns = [0] + [float('inf')] * (nums[0] - 1)
    for c in nums[1:]:
        d = gcd(nums[0], c)
        for r in range(d):
            n = min(ns[r::d], default=float('inf'))
            if n < float('inf'):
                for j in range(nums[0] // d):
                    n += c
                    p = n % nums[0]
                    ns[p] = n = min(n, ns[p])
    max_ = max(ns) or 1
    return max_ - nums[0] + 1 if max_ < float('inf') else -1
