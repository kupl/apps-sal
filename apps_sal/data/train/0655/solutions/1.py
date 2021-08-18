for _ in range(int(input())):
    n, k, v = list(map(int, input().split()))
    a = list(map(int, input().split()))
    s = v * (n + k)
    s -= sum(a)
    l = s // k
    if l < 1 or s % k != 0:
        print(-1)
    else:
        print(l)
