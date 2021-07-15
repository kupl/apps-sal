from math import gcd

a, res1, res2, memo = 6, [0], [1], {1}
for i in range(1, 1000000):
    x = a + gcd(i, a)
    a, g = x, x-a
    res1.append(res1[-1] + (g == 1))
    if g not in memo:
        res2.append(max(res2[-1], g))
        memo.add(g)

count_ones = res1.__getitem__
max_pn     = res2.__getitem__
an_over_average = lambda _: 3
