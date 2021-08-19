s = list(input())
n = len(s)
for i in range(n):
    if s[i] == '0':
        s.pop(i)
        break
if len(s) == n - 1:
    print(''.join(s))
else:
    print(''.join(s[0:n - 1]))
