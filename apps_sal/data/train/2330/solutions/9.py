def main():
    s = '0' + input()
    ans = []
    f = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            f = False
            break
    if s[1] == '0' or s[-2] == '0':
        f = False
    if f:
        ans = []
        p = len(s) - 1
        for i in reversed(range(1, len(s) - 1)):
            c = s[i]
            ans.append([i, p])
            if c == '1':
                p = i
        for (u, v) in ans:
            print(u, v)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
