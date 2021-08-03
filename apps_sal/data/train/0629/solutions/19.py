t = int(input())
for ijk in range(0, t):
    r, g, b, m = list(map(int, input().strip().split()))
    ra = list(map(int, input().strip().split()))
    rb = list(map(int, input().strip().split()))
    rc = list(map(int, input().strip().split()))
    a = [max(ra), max(rb), max(rc)]
    for i in range(0, m):
        j = a.index(max(a))
        a[j] = a[j] // 2
    print(max(a))
