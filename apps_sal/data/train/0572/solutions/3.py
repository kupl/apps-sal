t = int(input())
for i in range(t):
    n, m, k = list(map(int, input().split()))
    k1 = abs(n - m)
    if k <= k1:
        print(k1 - k)
    else:
        print(0)
