t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    l = list(map(int, input().split()))
    m = max(l)
    a = []
    for i in range(n):
        if(m == l[i]):
            a.append(i + 1)
    b = []
    for i in range(1, len(a)):
        b.append(a[i] - a[i - 1])
    if(len(a) > 1):
        b.append(n - a[-1] + a[0])
        k = max(b)
        if(k >= n // 2):
            print(k - (n // 2))
        else:
            print(0)
    else:
        print((n + 1) // 2)
