S = input()
T = input()
dps = [0] * len(S)
for i in range(len(S)):
    if S[i] == 'A':
        dps[i] += 1
    if i != 0:
        dps[i] += dps[i - 1]
dpt = [0] * len(T)
for i in range(len(T)):
    if T[i] == 'A':
        dpt[i] += 1
    if i != 0:
        dpt[i] += dpt[i - 1]
dps = [0] + dps
dpt = [0] + dpt
q = int(input())
for i in range(q):
    (a, b, c, d) = list(map(int, input().split()))
    sc = dps[b] - dps[a - 1]
    sa = sc - (b - a + 1 - sc)
    tc = dpt[d] - dpt[c - 1]
    ta = tc - (d - c + 1 - tc)
    if sa % 3 == ta % 3:
        print('YES')
    else:
        print('NO')
