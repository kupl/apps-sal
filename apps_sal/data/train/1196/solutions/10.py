t = int(input())
for ii in range(t):
    n, m, k = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        pp = [int(x) for x in input().split()]
        a.append(pp)
    arr = []
    for i in range(m):
        pp = []
        for j in range(n):
            pp.append(a[j][i])
        arr.append(pp)
    # print(a,arr)
    s = 0
    for i in a:
        for j in range(m - k + 1):
            s = max(s, sum(i[j:j + k]))
    for i in arr:
        for j in range(n - k + 1):
            s = max(s, sum(i[j:j + k]))
    print(s)
