from math import factorial
M = 10**9 + 7

for t in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    z = a.count(0)
    if z == 0:
        s = 0
        x = factorial(n)
        for i in range(k % 2, min(n, k) + 1, 2):
            s += ((x / factorial(i)) / factorial(n - i))
        s = s % M
        print(s)
    else:
        n = n - z
        s = 0
        x = factorial(n)
        for i in range(0, min(n, k) + 1):
            s += ((x / factorial(i)) / factorial(n - i))
        s = s % M
        print(s)
