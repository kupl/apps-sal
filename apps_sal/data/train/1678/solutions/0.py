(n, m) = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
max1 = arr1.index(max(arr1))
min2 = arr2.index(min(arr2))
arr = []
for i in range(m):
    arr.append([max1, i])
for i in range(n):
    if i != max1:
        arr.append([i, min2])
for i in arr:
    print(*i)
