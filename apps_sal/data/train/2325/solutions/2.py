def fc(x):
    return 1 if x == 'A' else 2


s = list(map(fc, list(input())))
t = list(map(fc, list(input())))
q = int(input())
abcd = [list(map(int, input().split())) for _ in range(q)]
cs = [0]
tmp = 0
for x in s:
    tmp += x
    cs.append(tmp)
ct = [0]
tmp = 0
for x in t:
    tmp += x
    ct.append(tmp)
for (a, b, c, d) in abcd:
    if (cs[b] - cs[a - 1]) % 3 == (ct[d] - ct[c - 1]) % 3:
        print('YES')
    else:
        print('NO')
