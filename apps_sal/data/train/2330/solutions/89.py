import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15


def main():
    S = input()
    N = len(S)
    if S[0] == '0' or S[-1] == '1':
        print(-1)
        return
    cnt = 0
    flag = True
    for i in range(N - 1):
        if S[i] != S[N - i - 2]:
            flag = False
            break
        if S[i] == '1':
            cnt += 1
    if not flag:
        print(-1)
        return
    edge = []
    for i in range(cnt):
        edge.append((i + 1, i + 2))
    extend = 0
    now = cnt + 2
    vertex = 2
    for i in range(1, N - 1):
        if S[i] == '0':
            extend += 1
        else:
            for _ in range(extend):
                edge.append((vertex, now))
                now += 1
            extend = 0
            vertex += 1
    if now == N + 1:
        print('\n'.join((' '.join(map(str, a)) for a in edge)))
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
