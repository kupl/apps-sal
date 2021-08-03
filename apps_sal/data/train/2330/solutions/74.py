# 01:36
s = input()
n = len(s)
if s[-1] == '1':
    print(-1)
    return
t = s[:-1]
if t[::-1] != t:
    print(-1)
    return
if s[0] == '0':
    print(-1)
    return
print(0 + 1, 1 + 1)
now = 0
for i in range(2, n):
    print(now + 1, i + 1)
    if s[i - 1] == '1':
        now = i
