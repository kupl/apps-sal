for i in range(int(input())):
    l, k = map(int, input().split())
    if k <= l:
        n = l - k + 1
        res = (n * (n + 1)) // 2
        print("Case " + str(i + 1) + ": " + str(res))
    else:
        print("Case " + str(i + 1) + ": " + str(0))
