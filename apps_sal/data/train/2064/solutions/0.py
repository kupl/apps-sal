import sys
readline = sys.stdin.readline

N, Q = list(map(int, readline().split()))
state = [[False]*(N+2) for _ in range(2)]

cnt = 0

Ans = [None]*Q
for qu in range(Q):
    r, c = list(map(int, readline().split()))
    r -= 1
    c -= 1
    state[r][c] = not state[r][c]
    res = state[r-1][c-1] + state[r-1][c] + state[r-1][c+1]  
    if state[r][c]:
        cnt += res
    else:
        cnt -= res
    Ans[qu] = 'No' if cnt else 'Yes'
print('\n'.join(Ans))

