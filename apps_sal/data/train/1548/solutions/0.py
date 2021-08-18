T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    left = [-1 for i in range(n)]
    right = [-1 for i in range(n)]
    min1 = float("inf")
    for i in range(n):
        min1 = min(arr[i], min1 + 1)
        left[i] = min1
    min1 = float("inf")
    for i in range(n - 1, -1, -1):
        min1 = min(arr[i], min1 + 1)
        right[i] = min1
    for i in range(n):
        print(min(left[i], right[i]), end=" ")
    print("", end="\n")
