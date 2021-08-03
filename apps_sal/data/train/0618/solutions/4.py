for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a[0:k])
    x = s
    for i in range(n - 1):
        s = s - a[i] + a[(i + k) % n]
        if x < s:
            x = s
    print(x)
