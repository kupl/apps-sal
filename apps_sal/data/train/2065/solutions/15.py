n, k = list(map(int, input().split()))
u = 0
for i in range(k):
    a = list(map(int, input().split()))[1:] + [0]
    if a[0] == 1:
        while a[u] == u + 1:
            u += 1
print(n + n - u - u - k + 1)
