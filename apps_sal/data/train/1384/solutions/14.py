# cook your dish here
for t in range(int(input())):
    n, k = map(int, input().split())

    arr = list(input())

    for i in range(len(arr)):
        arr[i] = int(arr[i])

    head = [0 for i in range(n)]

    for i in range(1, n):
        if arr[i - 1] == 0:
            head[i] = 0
        elif arr[i - 1] == 1:
            head[i] = head[i - 1] + 1

    tail = [0 for i in range(n)]

    for i in range(n - 2, -1, -1):
        if arr[i + 1] == 0:
            tail[i] = 0
        elif arr[i + 1] == 1:
            tail[i] = tail[i + 1] + 1

    ans = 0
    j = 0

    while j + k <= n:
        ans = max(ans, k + head[j] + tail[j + k - 1])
        j += 1
    print(ans)
