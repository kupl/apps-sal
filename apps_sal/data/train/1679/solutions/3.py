for ad in range(int(input())):
    (n, k, x) = list(map(int, input().split()))
    l = [0] * (k - 1)
    l.append(x)
    l = l * (n // k) + l
    l = l[:n]
    for i in range(n):
        print(l[i], end=' ')
    print()
