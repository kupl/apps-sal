from collections import deque


A = input()
N = len(A)
a = ord('a')

edge = [[N + 1] * 26 for _ in range(N + 1)]
for i in range(N - 1, -1, -1):
    for j in range(26):
        edge[i][j] = edge[i + 1][j]
    c = ord(A[i]) - a
    edge[i][c] = i + 1


recon = [None] * (N + 2)
q = deque()
q.append(0)
while q:
    i = q.popleft()
    if i == N + 1:
        break
    for j in range(26):
        ni = edge[i][j]
        if recon[ni] is None:
            recon[ni] = (i, chr(a + j))
            q.append(ni)

i = N + 1
ans = []
while i > 0:
    pi, c = recon[i]
    ans.append(c)
    i = pi

print((''.join(reversed(ans))))
