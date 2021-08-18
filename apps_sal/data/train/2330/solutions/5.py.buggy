s = input()
n = len(s)
ok = s[0] == '1' and s[n - 1] == '0'
for i in range(n - 1):
    ok = ok and s[i] == s[n - 2 - i]
if not ok:
    print((-1))
    return
s2 = s[:n // 2]
i = s2.rindex('1')
for k in range(i, n - 1):
    print((n, k + 1))
while i > 0:
    j = i - 1
    while s[j] != '1':
        j -= 1
    for k in range(j, i):
        print((i + 1, k + 1))
    i = j
