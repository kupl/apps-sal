import math
import copy
from functools import reduce
t = int(input())
for i in range(t):
    n = input()
    nums = list(map(int, input().split()))
    n = copy.deepcopy(nums)
    gc = reduce(lambda x, y: math.gcd(x, y), n)
    cost = sum([x // gc for x in nums])
    print(gc, cost)
