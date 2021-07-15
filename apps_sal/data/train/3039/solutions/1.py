nums = list(range(1, 10))
sums, rth = nums[:], []
for _ in range(30):
    nums_, sums_ = [], []
    for n, s in zip(nums, sums):
        for n_, s_ in enumerate(range(s, s+10), 10*n):
            if not n_ % s_:
                nums_.append(n_)
                sums_.append(s_)
    nums, sums = nums_, sums_
    rth.extend(nums)

from bisect import bisect
def rthn_between(a, b):
    return rth[bisect(rth, a-1): bisect(rth, b)]
