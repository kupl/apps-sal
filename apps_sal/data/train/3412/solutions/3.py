import math
import numpy as np


def f(n):
    if set(primeFactors(n).values()) == {1}:
        return 1
    return np.prod([v * k**(v - 1) for k, v in primeFactors(n).items()])   # (n_ = n*)


def primeFactors(n):
    ans = dict()
    cnt2 = 0
    while n % 2 == 0:
        cnt2 += 1
        ans.update({2: cnt2})
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        cnti = 0
        while n % i == 0:
            cnti += 1
            ans.update({i: cnti})
            n = n / i
    if n > 2:
        ans.update({n: 1})
    return ans
