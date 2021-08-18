for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    dinos = list(range(1, k + 1)) + [n] + list(range(k + 1, n))
    print(' '.join(map(str, dinos)))
