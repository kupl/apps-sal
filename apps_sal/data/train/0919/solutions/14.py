from collections import defaultdict as dd
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    stacks = dd(lambda: -10**9)
    c = temp = 0
    for i in a:
        temp = c
        c = max(c, stacks[i] + 1)
        stacks[i] = max(stacks[i], temp + 1)
    print(n - c)
