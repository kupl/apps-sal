def digitp(s):
    p = 1
    for i in range(len(s)):
        p *= int(s[i])
    return p


n = int(input())
cs = 0
cps = 0
for i in range(1, 10 ** 6 + 1):
    s = str(i)
    if digitp(s) == n:
        if '1' in s:
            cps += 1
        else:
            cs += 1
print(cs, cps)
