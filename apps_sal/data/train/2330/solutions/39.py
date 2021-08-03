import sys


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


S = '-' + sr()
N = len(S) - 1


def solve(S):
    if S[1] == '0' or S[N] == '1':
        return None
    prev = 1
    graph = []
    for i in range(1, N // 2 + 1):
        if S[i] != S[N - i]:
            return None
        if S[i] == '0':
            continue
        for x in range(prev, i):
            graph.append('{} {}'.format(x, i))
        prev = i
    for x in range(prev, N):
        graph.append('{} {}'.format(x, N))
    return graph


graph = solve(S)
if graph is None:
    print((-1))
else:
    print(('\n'.join(graph)))

# 42
