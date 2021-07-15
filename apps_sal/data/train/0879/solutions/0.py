for _ in range(int(input())):
    x, y = map(int, input().split())
    ans = 0
    for i in range(y, x+1, y):
        if i%y == 0:
            ans += i%10
    print(ans)
