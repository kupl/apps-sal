import sys
readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = '*' + input()
    N = len(S) - 1
    if S[N] == '1':
        return print(-1)
    if S[1] == '0':
        return print(-1)
    edge = []
    cur_u = 1
    cur_v = 2
    for i in range(1, N // 2 + 1):
        if S[i] != S[N - i]:
            return print(-1)
        edge.append([cur_u, cur_v])
        if S[i] == '1':
            cur_u = cur_v
        cur_v += 1
    for i in range(cur_v, N + 1):
        edge.append([cur_u, i])
    for i in range(N - 1):
        print(*edge[i])


def __starting_point():
    main()


__starting_point()
