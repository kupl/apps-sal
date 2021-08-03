def solve():
    n = int(input())
    s = input()
    z, o = [], []
    c = 0
    ans = []

    def add(x):
        nonlocal z, o, c, ans
        u, v = z, o
        if x == 0:
            u, v = v, u
        if u:
            w = u.pop()
            ans.append(w)
            v.append(w)
        else:
            c += 1
            ans.append(c)
            v.append(c)
    for i in s:
        add(int(i))
    print(c)
    print(*ans)


t = int(input())
for _ in range(t):
    solve()
