a, n, k = map(int, input().split())
arr = [0 for i in range(k)]
i = 0
while a != 0 and i < k:
    arr[i] = a % (n + 1)
    a = a // (n + 1)
    i += 1
for i in range(k):
    print(arr[i], end=' ')
