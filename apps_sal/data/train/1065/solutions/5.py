from itertools import combinations
from scipy.spatial.distance import pdist
import numpy as np


def solve():
    houses = []
    (n, m) = list(map(int, input().split()))
    for i in range(n):
        s = input()
        tmp = [i for (i, x) in enumerate(s) if x == '1']
        houses = houses + [[i, j] for j in tmp]
    counter = [0] * (n + m - 1)
    dis = pdist(np.array(houses), 'cityblock').astype(int)
    for i in dis:
        counter[i] += 1
    return [counter[i] for i in range(1, n + m - 1)]


for _ in range(int(input())):
    print(*solve())
