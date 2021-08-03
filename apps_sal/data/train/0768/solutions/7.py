# cook your dish here
import sys

sys.setrecursionlimit(10**6)


def recurse(root):
    if adj[root] == []:
        return 1, 1
    sub = 1
    max1 = 0
    for v in adj[root]:
        x, y = recurse(v)
        sub += x
        max1 = max(max1, y)
    return sub, sub + max1


for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []
    for i in range(n - 1):
        parent, child = p[i], i + 2
        adj[parent].append(child)
    x, y = recurse(1)
    print(y)
