n = int(input())
arr = []
for i in range(1, n + 1):
    arr.append(i)
c = 0
i = 0
f = 0
while c < n - 1:
    if arr[i % n] != -1 and f:
        arr[i % n] = -1
        c = c + 1
        f = 0
    if arr[i % n] != -1:
        f = 1
    i = i + 1
for i in range(0, n):
    if arr[i] != -1:
        ans = arr[i]
        break
print(ans)
