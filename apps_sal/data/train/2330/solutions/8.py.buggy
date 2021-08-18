s = input()
if s[-1] == '1':
    print(-1)
    return
if s[-2] == '0':
    print(-1)
    return

t = s[:-1]
D = []
for i in range((len(t) + 1) // 2):
    if t[i] != t[-1 - i]:
        print(-1)
        return
m = 1
A = []
for i in range(1, len(s) // 2 + 1):
    A.append((m, i + 1))
    if s[i - 1] == '1':
        m = i + 1
for i in range(len(s) // 2 + 2, len(s) + 1):
    A.append((m, i))
for i in A:
    print(*i)
