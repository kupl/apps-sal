s = input()
le = len(s)
m = [le] * (le + 1)
ans = 0
for i in range(le - 1, -1, -1):
    m[i] = m[i + 1]
    k = 1
    while k * 2 + i < m[i]:
        if s[i] == s[i + k] and s[i] == s[i + 2 * k]:
            m[i] = i + 2 * k
        k += 1
    ans += le - m[i]
print(ans)

