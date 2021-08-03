t = int(input())
for _ in range(t):
    n = list(map(int, input().split()))
    k = n[1]
    n = n[0]
    a = list(map(int, input().split()))
    m = -999999999999
    s1 = set(a)
    for i in range(0, n - k + 1):
        s = sum(a[i:i + k])
        if s > m and set(a[i:i + k]) == s1:
            m = s
    print(m)
