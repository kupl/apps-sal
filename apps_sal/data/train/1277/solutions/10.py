for i in range(int(input())):
    n = int(input())
    ans = 0
    for j in range(0, n):
        (p, q, d) = list(map(int, input().split()))
        ans += (p - (p + d * p / 100 - (p + d * p / 100) * (d / 100))) * q
    print('{0:.9f}'.format(ans))
