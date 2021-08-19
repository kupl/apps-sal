n = int(input())
a = list(map(int, input().split()))
k = 0
for i in range(0, n - 1, 2):
    k = k ^ a[i] ^ a[i + 1]
for i in range(n):
    print(k ^ a[i], end=' ')
