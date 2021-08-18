import math


def solve():

    n, k = list(map(int, input().split()))
    s = sorted(map(int, input().split()), reverse=True)
    while k < n and s[k - 1] == s[k]:
        k += 1
    print(k)


t = int(input())
for i in range(t):
    solve()
