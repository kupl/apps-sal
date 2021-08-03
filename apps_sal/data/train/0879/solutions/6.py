for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = 0
    y = a // b
    x = b
    for i in range(y):
        x = x % 10
        ans += x
        x += b
    print(ans)
