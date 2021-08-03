S, T, q, *L = open(0).read().split()
sa = [0]
sb = [0]
ta = [0]
tb = [0]
for c in S:
    if c == 'A':
        sa.append(sa[-1] + 1)
        sb.append(sb[-1])
    else:
        sa.append(sa[-1])
        sb.append(sb[-1] + 1)
for c in T:
    if c == 'A':
        ta.append(ta[-1] + 1)
        tb.append(tb[-1])
    else:
        ta.append(ta[-1])
        tb.append(tb[-1] + 1)
for a, b, c, d in zip(*[iter(map(int, L))] * 4):
    nsa = sa[b] - sa[a - 1]
    nsb = sb[b] - sb[a - 1]
    nta = ta[d] - ta[c - 1]
    ntb = tb[d] - tb[c - 1]
    mb = ntb - nsb
    ma = nta - nsa
    if (2 * mb + ma) % 3 == (2 * ma + mb) % 3 == 0:
        print('YES')
    else:
        print('NO')
