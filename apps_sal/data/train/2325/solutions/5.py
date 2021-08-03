
S = input()
T = input()

sa = [0]
sb = [0]
ta = [0]
tb = [0]

for i in S:
    if i == "A":
        sa.append(sa[-1] + 1)
        sb.append(sb[-1])
    else:
        sa.append(sa[-1])
        sb.append(sb[-1] + 1)

for i in T:
    if i == "A":
        ta.append(ta[-1] + 1)
        tb.append(tb[-1])
    else:
        ta.append(ta[-1])
        tb.append(tb[-1] + 1)


q = int(input())

for i in range(q):

    a, b, c, d = list(map(int, input().split()))

    one = ((sa[b] - sa[a - 1]) - (sb[b] - sb[a - 1]))
    two = ((ta[d] - ta[c - 1]) - (tb[d] - tb[c - 1]))

    if one % 3 == two % 3:
        print("YES")
    else:
        print("NO")
