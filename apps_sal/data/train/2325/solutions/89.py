import sys


def input():
    return sys.stdin.readline().rstrip()


def yes():
    print("YES")


def no():
    print("NO")


def solve():
    S = input()
    T = input()
    lenS = len(S)
    lenT = len(T)
    Q = int(input())
    Query = [tuple(map(int, input().split())) for i in range(Q)]
    S_cnt = [0] * (lenS + 1)
    T_cnt = [0] * (lenT + 1)
    for i in range(lenS):
        if S[i] == "A":
            S_cnt[i + 1] += 1
        else:
            S_cnt[i + 1] -= 1
    for i in range(lenS):
        S_cnt[i + 1] += S_cnt[i]

    for i in range(lenT):
        if T[i] == "A":
            T_cnt[i + 1] += 1
        else:
            T_cnt[i + 1] -= 1
    for i in range(lenT):
        T_cnt[i + 1] += T_cnt[i]

    for a, b, c, d in Query:
        modS = (S_cnt[b] - S_cnt[a - 1]) % 3
        modT = (T_cnt[d] - T_cnt[c - 1]) % 3
        if modS == modT:
            yes()
        else:
            no()
    return


solve()
