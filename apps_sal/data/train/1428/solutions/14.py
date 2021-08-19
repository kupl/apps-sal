from collections import deque
import math


def solve(nums, d, z):
    q1 = deque(sorted(nums, reverse=True))
    q2 = deque()
    c = 0
    if d >= z:
        return c
    while True:
        if len(q1) == 0 and len(q2) == 0:
            break
        if not q2 or q1[0] > q2[0]:
            ele = q1.popleft()
            c += 1
            d += ele
            if d >= z:
                return c
            ele = ele // 2
            if ele >= 1:
                q2.append(ele)
        else:
            ele = q2.popleft()
            c += 1
            d += ele
            if d >= z:
                return c
            ele = ele // 2
            if ele >= 2:
                q2.append(ele)
        if not q1:
            (q1, q2) = (q2, q1)
    if d >= z:
        return c
    return 'RIP'


t = int(input())
for _ in range(t):
    (n, a, b, x, y, z) = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    queries = set([])
    c = z - b
    c = math.ceil(c / y) - 1
    d = a + x * c
    if d >= z:
        print(0)
    else:
        print(solve(nums, d, z))
