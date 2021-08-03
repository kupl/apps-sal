from math import gcd


def largest_factor(val, n):
    k = min(n, val)
    while k > 0:
        if val % k == 0:
            return k
        k -= 1


for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    li = list(map(int, input().split()))
    if n == 1:
        print(0)
    else:
        val = li[0]
        for i in range(1, m):
            val = gcd(val, li[i])
        print(n - largest_factor(val, n))
