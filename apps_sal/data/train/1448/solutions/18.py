for i in range(int(input())):
    a1, d, k, n, inc = list(map(int, input().split()))
    a = [a1]
    for i in range(1, n):
        if((i) % k == 0):
            d += inc
        a.append(a[i - 1] + d)
    print(a[n - 1])
