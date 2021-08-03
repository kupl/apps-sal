def ex(): print(-1); return


s = input()
N = len(s)
if not (s[0] == '1' and s[-1] == '0'):
    ex()
for i in range(N // 2):
    if s[i] != s[N - i - 2]:
        ex()
ans = []
m = 1
for i in range(1, N // 2 + 1):
    ans.append((m, i + 1))
    if s[i - 1] == '1':
        m = i + 1
for i in range(N // 2 + 2, N + 1):
    ans.append((m, i))
for t in ans:
    print(*t)
