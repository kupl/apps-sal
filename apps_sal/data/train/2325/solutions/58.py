s = list(input())
t = list(input())
ls, lt = len(s), len(t)
sa, sb = [0] * (ls + 1), [0] * (ls + 1)
ta, tb = [0] * (lt + 1), [0] * (lt + 1)
for i in range(1, ls + 1):
    if s[i - 1] == "A":
        sa[i] = sa[i - 1] + 1
        sb[i] = sb[i - 1]
    else:
        sa[i] = sa[i - 1]
        sb[i] = sb[i - 1] + 1
for i in range(1, lt + 1):
    if t[i - 1] == "A":
        ta[i] = ta[i - 1] + 1
        tb[i] = tb[i - 1]
    else:
        ta[i] = ta[i - 1]
        tb[i] = tb[i - 1] + 1

q = int(input())
for _ in range(q):
    ans = 0
    a, b, c, d = map(int, input().split())
    a1, b1 = sa[b] - sa[a - 1], sb[b] - sb[a - 1]
    a2, b2 = ta[d] - ta[c - 1], tb[d] - tb[c - 1]
    x, y = a1 - b1, a2 - b2
    if x * y < 0:
        x = -2 * x
    if abs(x - y) % 3 == 0:
        ans = 1
    print("YES" if ans == 1 else "NO")
