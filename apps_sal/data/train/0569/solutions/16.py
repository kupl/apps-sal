from collections import defaultdict
import math
p = int(input())
while p > 0:
    n = int(input())
    t = math.floor((2 * n + 1) ** 0.5 + 0.5)
    res = 0.5 * (t - t ** 2 + 2 * n)
    print(int(res))
    p -= 1
