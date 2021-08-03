for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mod = a[0] % a[1]
    for i in range(1, n):
        if mod > a[i]:
            mod = a[i] % mod
        else:
            mod = mod % a[i]
    print(mod)
