import sys
s = input()
n = len(s)
if s[-1] == '1':
    print(-1)
    return
if s[0] == '0':
    print(-1)
    return
for i in range(n - 1):
    if s[i] != s[n - 2 - i]:
        print(-1)
        return
ans = ['1', '2']
print(' '.join(ans))
current = 2
for i in range(1, n - 1):
    ans = []
    ans.append(str(current))
    ans.append(str(i + 2))
    print(' '.join(ans))
    if s[i] == '1':
        current = i + 2
