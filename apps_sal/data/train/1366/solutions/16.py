for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    x = 0
    iss = set()
    for i in range(n):
        if arr[i] == 0:
            x += 1
            iss.add(i)
        else:
            break
    for i in range(n - 1, -1, -1):
        if arr[i] == 0 and i not in iss:
            x += 1
        else:
            break
    print(max(1, n - x))
