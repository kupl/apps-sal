for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if len(arr) <= 1:
        print(0)
        continue
    mx = 0
    narr = [0]
    narr.append(0 if arr[1] != arr[0] else 1)
    for i in range(2, n):
        if arr[i - 2] == arr[i] and arr[i - 1] == arr[i]:
            narr.append(max(narr[-2], narr[-1]) + 1)
        elif arr[i - 1] == arr[i]:
            narr.append(narr[-1] + 1)
        elif arr[i - 2] == arr[i]:
            narr.append(narr[-2] + 1)
        else:
            narr.append(0)
        mx = max(mx, narr[-1])
    print(mx)
