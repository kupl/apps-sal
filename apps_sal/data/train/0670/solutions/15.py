from fractions import gcd
t = eval(input())
for _ in range(t):
    n = eval(input())
    a = [int(x) for x in input().strip().split()]
    s = a[0]
    for i in range(1, n):
        s = gcd(s, a[i])
    print(s * n)
