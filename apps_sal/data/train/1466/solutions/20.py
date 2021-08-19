(n, q) = map(int, input().split())
f = list(map(int, input().split()))
for j in range(1, n):
    f[j] ^= f[j - 1]
for g in range(q):
    k = int(input())
    tyagibagi = k % (n + 1)
    if tyagibagi == 0:
        print(0)
    else:
        print(f[tyagibagi - 1])
