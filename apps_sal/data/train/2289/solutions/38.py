import os
import sys
if os.getenv('LOCAL'):
    sys.stdin = open('_in.txt', 'r')
sys.setrecursionlimit(2147483647)
INF = float('inf')
IINF = 10 ** 18
MOD = 10 ** 9 + 7
S = sys.stdin.readline().rstrip()
A = [ord(c) - ord('a') for c in S]
N = len(S)
l = 0
lengths = [0] * N
counts = [0] * 26
for (i, a) in reversed(list(enumerate(A))):
    counts[a] += 1
    lengths[i] = l
    if min(counts) == 1:
        counts = [0] * 26
        l += 1
ans_size = l + 1
graph = [[-1] * 26 for _ in range(N)]
pos = [-1] * 26
for (i, a) in reversed(list(enumerate(A))):
    graph[i] = pos[:]
    pos[a] = i
initials = pos


def solve(size, i=None):
    if i is None:
        pos = initials
    else:
        pos = graph[i]
    if size == 1:
        return chr(pos.index(-1) + ord('a'))
    size -= 1
    for (ci, i) in enumerate(pos):
        if lengths[i] < size:
            c = chr(ci + ord('a'))
            return c + solve(size, i)
    assert False


print(solve(ans_size))
