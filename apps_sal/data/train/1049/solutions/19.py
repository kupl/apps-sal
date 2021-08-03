# cook your dish here
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    slen = len(set(a))
    lmax = -9
    for i in range(n - k + 1):
        x = set(a[i:i + k])
        if len(x) == slen:
            add = sum(a[i:i + k])
            if add > lmax:
                lmax = add
    print(lmax)
