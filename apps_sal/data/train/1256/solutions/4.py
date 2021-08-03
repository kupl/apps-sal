from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    ls = [int(x) for x in input().split()]
    n -= ls.count(1)
    n -= ls.count(0)
    twos = ls.count(2)
    ans = n * (n - 1) // 2
    if twos > 1:
        ans -= (twos - 1) * twos // 2
    print(ans)
