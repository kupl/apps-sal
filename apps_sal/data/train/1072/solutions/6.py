from math import sqrt as S
for _ in range(int(input())):
    n = int(input())
    a1 = int(S(n))
    a2 = n // a1
    rem = n - a1 * a2
    ans = ['X'] * a1 + ['D'] * a2
    if rem:
        ans.insert(-rem, 'X')
    print(*ans, sep='')
    maxi = 1
    for i in range(2, int(S(n)) + 1):
        if n % i == 0:
            maxi = max(maxi, i)
