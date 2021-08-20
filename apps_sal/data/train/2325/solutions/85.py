s = input()
t = input()
q = int(input())
ans = ['YES'] * q
scnt = [[0] * (len(s) + 1) for _ in range(2)]
tcnt = [[0] * (len(t) + 1) for _ in range(2)]
for (i, S) in enumerate(s):
    scnt[0][i + 1] = scnt[0][i]
    scnt[1][i + 1] = scnt[1][i]
    scnt[ord(S) - ord('A')][i + 1] += 1
for (i, T) in enumerate(t):
    tcnt[0][i + 1] = tcnt[0][i]
    tcnt[1][i + 1] = tcnt[1][i]
    tcnt[ord(T) - ord('A')][i + 1] += 1
for i in range(q):
    (a, b, c, d) = list(map(int, input().split()))
    a -= 1
    c -= 1
    A = scnt[0][b] - scnt[0][a] - tcnt[0][d] + tcnt[0][c]
    B = scnt[1][b] - scnt[1][a] - tcnt[1][d] + tcnt[1][c]
    if (A - B) % 3 != 0:
        ans[i] = 'NO'
print('\n'.join(ans))
