t = int(input())
for _ in range(t):
    n = int(input())
    res = 'abcdefghijklmnopqrstuvwxyz'
    ans = ''
    while True:
        ans = res[n::-1] + ans
        if n < 26:
            break
        else:
            n -= 25
    print(ans)
