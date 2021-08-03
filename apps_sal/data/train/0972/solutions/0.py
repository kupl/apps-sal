try:
    a = list(map(int, input().split()))
    n = a[0]
    k = a[1]
    hi = []
    for i in range(n):
        hi.append(int(input()))
    hi.sort()
    diff = []
    for i in range(n - k + 1):
        diff.append(hi[i + k - 1] - hi[i])
    print(min(diff))
except:
    pass
