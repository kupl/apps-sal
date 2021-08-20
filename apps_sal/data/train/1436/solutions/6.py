for _ in range(int(input())):
    s = input()
    n = len(s)
    ans = len(set(s))
    if ans == 1:
        print(1)
    else:
        (a, b, f) = (0, -1, 0)
        for i in range(n // 2):
            if s[a] != s[b]:
                print(ans)
                f = 1
                break
        if f == 0:
            print(1)
