import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

S = list(sr())
N = len(S)
if S[-1] == '1' or S[0] == '0' or S[:-1] != S[:-1][::-1]:
    print((-1)); return
S = ['-'] + S

def solve(S):
    prev = 1
    graph = []
    for i in range(1, N//2 + 1):
        if S[i] == '0':
            continue
        for x in range(prev, i):
            print((x, i))
        prev = i
    for x in range(prev, N):
        print((x, N))

graph = solve(S)

