t = int(input())
for i in range(t):
    n, m, k = list(map(int, input().split()))
    if(n > m):
        ma = n
        mi = m
        d = n - m
    elif(m > n):
        ma = m
        mi = n
        d = m - n
    else:
        d = 0
    if(d <= k):
        print(0)
    else:
        mi = mi + k
        print(ma - mi)
