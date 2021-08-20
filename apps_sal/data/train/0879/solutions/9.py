for t in range(int(input())):
    (x, y) = map(int, input().split())
    ans = 0
    for i in range(y, x + 1, y):
        ans += int(str(i)[-1])
    print(ans)
