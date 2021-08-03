for _ in range(int(input())):
    n = int(input())
    s = input()
    d = {}
    for i in s:
        try:
            d[i] += 1
        except:
            d[i] = 1
    ans = 1000000000
    for i in range(1, 9):
        x = str(i)
        try:
            ans = min(ans, d[x])
        except:
            ans = 0
    print(ans)
