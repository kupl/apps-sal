import math
t = int(input())
while t != 0:
    t -= 1
    ans = 0
    (n, x) = map(int, input().split())
    l = list(map(int, input().split()))
    a = []
    a.append(0)
    for i in range(n):
        a.append(l[i] + a[i])
    for i in range(1, int(math.sqrt(x) + 1)):
        if x % i is 0:
            y = x / i
            m = {}
            for j in range(i, n + 1):
                if a[j] - a[j - i] in m:
                    m[a[j] - a[j - i]] += 1
                else:
                    m[a[j] - a[j - i]] = 1
            for j in range(i, n + 1):
                z = y - (a[j] - a[j - i])
                if z in m:
                    ans += m[a[j] - a[j - i]] * m[z]
                    if a[j] - a[j - i] == z:
                        m[a[j] - a[j - i]] = 0
    print(ans)
