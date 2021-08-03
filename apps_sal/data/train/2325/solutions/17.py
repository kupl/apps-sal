def main():
    s = input()
    t = input()
    a = [0] * (len(s) + 1)
    b = [0] * (len(t) + 1)
    for i, c in enumerate(s):
        if c == "A":
            a[i + 1] = 1
        else:
            a[i + 1] = 2
        a[i + 1] += a[i]
    for i, c in enumerate(t):
        if c == "A":
            b[i + 1] = 1
        else:
            b[i + 1] = 2
        b[i + 1] += b[i]
    q = int(input())
    ans = [None] * q
    for i in range(q):
        a1, a2, b1, b2 = map(int, input().split())
        x, y = a[a2] - a[a1 - 1], b[b2] - b[b1 - 1]
        if abs(x - y) % 3 == 0:
            ans[i] = "YES"
        else:
            ans[i] = "NO"
    for v in ans:
        print(v)


def __starting_point():
    main()


__starting_point()
