from collections import defaultdict
from itertools import combinations
from scipy.spatial.distance import pdist


def solve():
    houses = []
    n, m = list(map(int, input().split()))

    for i in range(n):
        s = input()
        tmp = [i for i, x in enumerate(s) if x == '1']
        houses = houses + [(i, j) for j in tmp]

    counter = defaultdict(int)
    dis = pdist(houses, 'cityblock')
    for i in dis:
        counter[i] += 1
    return [counter[i] for i in range(1, n + m - 1)]


for _ in range(int(input())):
    print(*solve())
