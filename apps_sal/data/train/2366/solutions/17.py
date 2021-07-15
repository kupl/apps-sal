t = int(input())
for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    m = a[-1]
    res = 0
    
    for i in range(n-1, -1, -1):
        if a[i] > m:
            res += 1
        m = min(m, a[i])

    print(res)



