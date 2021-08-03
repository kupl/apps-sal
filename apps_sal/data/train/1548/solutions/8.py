t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    s = []
    p = []
    p.append(a[0])
    for i in range(1, n):
        p.append(min(p[i - 1] + 1, a[i]))
    s.append(a[n - 1])
    j = n - 2
    l = 0
    while(j >= 0):
        s.append(min(s[l] + 1, a[j]))
        j = j - 1
        l = l + 1
    t = s[::-1]
    for k in range(n):
        print(min(t[k], p[k]), end=" ")
    print("")
