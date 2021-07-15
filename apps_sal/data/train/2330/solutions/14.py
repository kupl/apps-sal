s = input()
n = len(s)
if s[0] == '0':
    print(-1)
    return
if s[-1] == '1':
    print(-1)
    return
for i in range((n - 1) // 2):
    if s[i] != s[n - i - 2]:
        print(-1)
        return
p = 1
t = 2
i = n - 2
while i >= 0:
    print(p, t)
    if s[i] == '1':
        p = t
    t += 1
    i -= 1
