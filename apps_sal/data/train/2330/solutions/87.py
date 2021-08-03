def main():
    s = input()
    n = len(s)
    res = []
    if s[0] == "0" or s[-1] == "1":
        print(-1)
        return 1
    m = n // 2
    t = m
    for i in range(m, 0, -1):
        if s[i - 1] != s[n - i - 1]:
            print(-1)
            return 1
        if i == m:
            if s[i - 1] == "1":
                res.append([m, m + 1])
                for j in range(m + 2, n + 1):
                    res.append([m + 1, j])
            else:
                for j in range(m + 1, n + 1):
                    res.append([m, j])
        else:
            if s[i - 1] == "1":
                res.append([t, i])
                t = i
            else:
                res.append([t, i])
    for sres in res:
        print(" ".join(map(str, sres)))


main()
