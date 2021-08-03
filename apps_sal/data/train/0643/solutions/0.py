

d = 10**9 + 7

t = int(input())
while t:
    t -= 1
    n = int(input())
    p = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    ans = 1
    for i in range(n):
        c = a[i] - b[i] + 1
        tmp = ((pow(p[i], b[i], d) * ((pow(p[i], c, d) - 1 + d) % d) * pow(p[i] - 1, d - 2, d) % d))
        ans *= tmp
        ans = ans % d

    print(ans)
