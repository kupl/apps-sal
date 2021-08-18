def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l = list(set(l))
    n = len(l)
    if(len(l) == 1):
        print(l[0] * 2)
    p = [0 for x in range(n)]
    s = [0 for x in range(n)]
    ans1 = 0
    p[0] = l[0]
    for i in range(1, n):
        p[i] = gcd(l[i], p[i - 1])
    s[n - 1] = l[n - 1]
    for i in range(n - 2, -1, -1):
        s[i] = gcd(l[i], s[i + 1])
    for i in range(n):
        if(i == 0):
            ans = s[i + 1] + l[0]
        elif(i == n - 1):
            ans = p[n - 2] + l[n - 1]
        else:
            ans = gcd(p[i - 1], s[i + 1]) + l[i]
        ans1 = max(ans1, ans)
    print(ans1)
