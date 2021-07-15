for _ in range(int(input())):
    n, d = list(map(int, input().split()))
    li = list(map(int, input().split()))
    res = li[0]
    for i in range(1, n):
        x = min(li[i], d // i)
        res += x
        d -= x * i
    print(res)

