s = list(input())
s = [int(si) for si in s]
n = len(s)
if s[-1] or not s[0]:
    print(-1)
    return
for i in range(1, n // 2):
    if s[i - 1] != s[n - i - 1]:
        print(-1)
        return
ans = [(1, 2)]
for i in range(1, n - 1):
    x, y = ans[-1]
    if s[i]:
        ans.append((y, i + 2))
    else:
        ans.append((i + 2, y))
for x, y in ans:
    print(x, y)
