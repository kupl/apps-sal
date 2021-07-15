from math import gcd
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(max(l[0], l[n-1]))

