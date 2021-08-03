from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    ls = [int(x) for x in input().split()]
    n -= (ls.count(1) + ls.count(0))
    twos = ls.count(2)
    rest = twos * (n - twos) + ((n - twos) * (n - twos - 1)) // 2
    print(rest)
