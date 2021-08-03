p = int(input())
for j in range(p):
    a, d, k, n, inc = list(map(int, input().split()))
    l = [a]
    for i in range(2, n + 1):
        a = a + d
        l.append(a)
        if(i % k == 0):
            d = d + inc
    print(l[n - 1])
