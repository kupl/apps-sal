import sys


def I():
    return int(sys.stdin.readline().rstrip())


def MI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


(S, T) = (S(), S())
(a, b) = (0, 0)
accumulate_S = [0]
accumulate_T = [0]
for s in S:
    if s == 'A':
        a += 1
    else:
        a += 2
    accumulate_S.append(a)
for t in T:
    if t == 'A':
        b += 1
    else:
        b += 2
    accumulate_T.append(b)
q = I()
for _ in range(q):
    (a, b, c, d) = MI()
    x = accumulate_S[b] - accumulate_S[a - 1]
    y = accumulate_T[d] - accumulate_T[c - 1]
    if (x - y) % 3 == 0:
        print('YES')
    else:
        print('NO')
