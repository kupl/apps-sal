#!/usr/bin/env python3
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(item) for item in input().split()]
    kind = len(set(a))
    # Single animal
    if kind == 1:
        ans = [1] * n
        print(1)
        print(*ans)
        continue
    # Has sequence
    a.append(a[0])
    l = 0
    has_sequence = False
    for i, (a1, a2) in enumerate(zip(a, a[1:])):
        if a1 == a2:
            l = i
            has_sequence = True
            break
    # All different
    if not has_sequence:
        if n % 2 == 0:
            ans = [1, 2] * (n // 2)
            print(2)
            print(*ans)
        else:
            ans = [1, 2] * (n // 2) + [3]
            print(3)
            print(*ans)
        continue
    if n % 2 == 0:
        ans = [1, 2] * (n // 2)
        print(2)
        print(*ans)
    else:
        ans = [1, 2] * (n // 2)
        if l == n - 1:
            ans.append(ans[0])
        else:
            ans.insert(l, ans[l])
        print(2)
        print(*ans)
