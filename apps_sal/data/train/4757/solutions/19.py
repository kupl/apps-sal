import math
t = int(input())


def convert(s):
    new = ''
    for x in s:
        new += x
    return new


for i in range(t):
    (n, m, a, b) = map(int, input().split())
    if m * b != n * a:
        print('NO')
    else:
        print('YES')
        l = 0
        for j in range(n):
            ans = ['0'] * m
            for k in range(a):
                ans[(l + k) % m] = '1'
            print(convert(ans))
            l += math.gcd(a, m)
