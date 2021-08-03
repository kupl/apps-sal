for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    c = 0
    s = 0
    for i in range(n):
        s += (a[i] - c - 1) // k
        c = a[i]
    print(s)
