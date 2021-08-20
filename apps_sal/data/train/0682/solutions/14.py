n = int(input())
arr = list(map(int, input().split()))
brr = []
(l, r) = (0, 0)
i = 0
while i < n:
    if arr[i] != i + 1:
        (l, r) = (i + 1, arr[i])
        break
    i += 1
while i < r:
    if arr[i] != l + r - i - 1:
        (l, r) = (0, 0)
        break
    i += 1
while i < n:
    if arr[i] != i + 1:
        (l, r) = (0, 0)
        break
    i += 1
print(l, r)
