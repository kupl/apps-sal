tc = int(input())
for it in range(tc):
    n, k, m = list(map(int, input().split()))
    cnt = 0
    cntr = k + m
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    for it1 in range(m):
        c.append(d[it1])
    for j in range(n):
        a[j] = a[j] - b[j]
        cnt = cnt + a[j]
    a.sort()
    c.sort()
    while(n > 0 and cntr > 0):
        if(a[n - 1] >= c[cntr - 1]):
            cnt = cnt - c[cntr - 1]
            cntr = cntr - 1
            n = n - 1
        else:
            cntr = cntr - 1
    print(cnt)
