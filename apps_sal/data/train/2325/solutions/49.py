import sys
input = sys.stdin.readline


def make_acc(U):
    res = [0]
    for (i, u) in enumerate(U):
        res.append((res[-1] + (1 if u == 'A' else 2)) % 3)
    return res


def judge(acc, p, q):
    return (acc[q] - acc[p - 1]) % 3


S = input()
T = input()
(S_acc, T_acc) = (make_acc(S), make_acc(T))
Q = int(input())
for _ in range(Q):
    (a, b, c, d) = list(map(int, input().split()))
    print('YES' if judge(S_acc, a, b) == judge(T_acc, c, d) else 'NO')
