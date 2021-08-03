for _ in range(int(input())):
    s = input()
    n = len(s)
    if len(s) == s.count("0") or len(s) == s.count("1"):
        print(-1)
    else:
        if n % 2 == 0:
            x = abs(n - 2 * (s.count("0")))
            print(x // 2)
        else:
            print(-1)
