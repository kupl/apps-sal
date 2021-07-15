S = input()
T = input()

cum_s = [(0, 0)]
cum_t = [(0, 0)]

for i in range(len(S)):
    p, q = cum_s[-1]
    if S[i] == 'A':
        cum_s.append((p + 1, q))
    else:
        cum_s.append((p, q + 1))

for i in range(len(T)):
    p, q = cum_t[-1]
    if T[i] == 'A':
        cum_t.append((p + 1, q))
    else:
        cum_t.append((p, q + 1))

Q = int(input())

for _ in range(Q):
    a, b, c, d = map(int, input().split())
    sp = cum_s[b][0] - cum_s[a - 1][0]
    sq = cum_s[b][1] - cum_s[a - 1][1]
    tp = cum_t[d][0] - cum_t[c - 1][0]
    tq = cum_t[d][1] - cum_t[c - 1][1]
    sp += sq * 2
    tp += tq * 2
    if sp % 3 == tp % 3:
        print('YES')
    else:
        print('NO')
