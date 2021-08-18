import collections
from collections import defaultdict
import math


for _ in range(int(input())):

    p1, p2, k = [int(x) for x in input().split()]

    r = math.floor((p1 + p2) / k)
    if r % 2 == 0:
        print("CHEF")
    else:
        print("COOK")
