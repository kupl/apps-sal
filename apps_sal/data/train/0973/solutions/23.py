for _ in range(int(input())):
    (n, k) = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    if arr[0] >= 0:
        arr[0] = arr[0] + k
    elif arr[0] < 0:
        arr[0] -= k
    if arr[len(arr) - 1] >= 0:
        arr[len(arr) - 1] -= k
    elif arr[len(arr) - 1] < 0:
        arr[len(arr) - 1] -= k
    print(abs(arr[0] - arr[len(arr) - 1]))
