def temple(n, arr):
    s = sum(arr)
    left = [0] * n
    right = [0] * n
    left[0] = 1
    right[-1] = 1
    maxHeight = 0
    for i in range(1, n):
        left[i] = min(left[i - 1] + 1, arr[i])
    for i in range(n - 2, -1, -1):
        right[i] = min(right[i + 1] + 1, arr[i])
    for i in range(n):
        maxHeight = max(maxHeight, min(left[i], right[i]))
    print(s - maxHeight ** 2)


for _ in range(int(input())):
    temple(int(input()), list(map(int, input().split())))
