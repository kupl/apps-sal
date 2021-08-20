t = int(input())
for _ in range(t):
    p = list(map(int, input().split()))
    n = p[0]
    k = p[1]
    l = list(map(int, input().split()))
    s = 0
    f = 1
    for i in range(0, n):
        s += l[i]
        if s < k:
            print(i + 1)
            f = 0
            break
        s = s - k
    if f:
        print(sum(l) // k + 1)
