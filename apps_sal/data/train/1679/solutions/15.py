for _ in range(int(input())):
    (n, k, x) = list(map(int, input().split()))
    l = [0] * n
    for i in range(0, n, k):
        l[i] = x
    l = list(map(str, l))
    print(' '.join(l))
