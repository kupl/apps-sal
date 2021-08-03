s = input()

a = 0
l = len(s)
for i in range(l):
    k = 0
    m = 0
    for j in range(i, l):
        m += s[j] == '('
        m -= s[j] == ')'
        k += s[j] == '?'
        if m + k < 0:
            break
        if k > m:
            m, k = k, m
        if m == k:
            a = a + 1
print(a)
