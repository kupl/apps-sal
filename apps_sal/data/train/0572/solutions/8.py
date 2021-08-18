N = int(input())
for i in range(N):
    n, m, k = [int(x) for x in input().split()]
    y = min(n, m)
    z = max(n, m)
    if y + k >= z:
        print(0)
    else:
        print(z - (y + k))
