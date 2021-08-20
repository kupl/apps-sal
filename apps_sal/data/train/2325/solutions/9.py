s = input()
S = [0]
d = 0
for i in s:
    if i == 'A':
        d += 1
    else:
        d += 2
    S.append(d)
t = input()
T = [0]
d = 0
for i in t:
    if i == 'A':
        d += 1
    else:
        d += 2
    T.append(d)
q = int(input())
for i in range(q):
    (a, b, c, d) = map(int, input().split())
    x = S[b] - S[a - 1]
    y = T[d] - T[c - 1]
    if (x - y) % 3 == 0:
        print('YES')
    else:
        print('NO')
