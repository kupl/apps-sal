import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

S = '-' + sr()
N = len(S) - 1
def solve(S):
    if S[1] == '0':
        print((-1)); return
    if S[N] == '1':
        print((-1)); return
    prev = 1
    graph = []
    for n in range(1,N//2 + 1):
        if S[n] != S[N-n]:
            print((-1)); return
        if S[n] == '0':
            continue
        for i in range(prev,n):
            graph.append('{} {}'.format(i,n))
        prev = n
    for i in range(prev,N):
        graph.append('{} {}'.format(i,N))
    return graph

graph = solve(S)

if graph is None:
    print((-1))
else:
    print(('\n'.join(graph)))

