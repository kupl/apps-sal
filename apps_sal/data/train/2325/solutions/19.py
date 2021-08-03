import sys
input = sys.stdin.readline


def solve():
    S, T = input(), input()
    q = int(input())

    ls, lt = len(S), len(T)
    acs, act = [0] * (ls + 1), [0] * (lt + 1)

    for i in range(1, ls + 1):
        acs[i] = acs[i - 1] + (S[i - 1] == "A")
    for i in range(1, lt + 1):
        act[i] = act[i - 1] + (T[i - 1] == "A")

    for _ in range(q):
        a, b, c, d = list(map(int, input().split()))
        print(("YES" if (acs[b] - acs[a - 1] + b - a + 1) % 3 == (act[d] - act[c - 1] + d - c + 1) % 3 else "NO"))


solve()
