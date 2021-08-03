s = input()
l = list()
cur = 0
for i in range(len(s)):
    if s[i] == 'a':
        cur += 1
    else:
        l.append(cur)

mo = 10**9 + 7

cur = 0
exp = 1
res = 0
for i in range(len(l)):
    while l[i] > cur:
        cur += 1
        exp = exp * 2 % mo
    res = (res + exp - 1) % mo


print(res)
