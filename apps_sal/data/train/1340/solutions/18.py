for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    p = 0
    ans = 0
    x = []
    for i in range(n):
        if arr[i] >= 0:
            p += 1
            ans += arr[i]

    for i in range(p):
        if arr[i] < 0:
            x.append(i + 1)
    for i in range(p, n):
        if arr[i] >= 0:
            x.append(i + 1)
    print(ans)
    print(len(x), end=' ')
    for i in x:
        print(i, end=' ')
    print()
