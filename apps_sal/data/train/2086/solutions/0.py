import sys
input = sys.stdin.readline


from collections import deque
N, Q = list(map(int, input().split()))
que = deque([int(a) for a in input().split()])
ma = max(que)

X = []
k = -1
c = 0
while c <= k+N+5:
    a = deque.popleft(que)
    b = deque.popleft(que)
    
    X.append((a, b))
    c += 1
    if a > b:
        a, b = b, a
    if k < 0 and b == ma:
        k = c
    deque.appendleft(que, b)
    deque.append(que, a)

for _ in range(Q):
    i = int(input()) - 1
    if i <= k:
        print(*X[i])
    else:
        i = (i-k)%(N-1)+k
        print(*X[i])


