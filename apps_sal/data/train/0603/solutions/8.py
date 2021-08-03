for t in range(int(input())):
    n = int(input())
    s, ans = "abcdefghijklmnopqrstuvwxyz", ""
    while True:
        ans = s[n::-1] + ans
        if n < 26:
            break
        else:
            n -= 25
    print(ans)
