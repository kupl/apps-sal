s = input()
n = len(s)
a = [n] * (n + 1)
ans = 0
for i in range(n - 1, -1, -1):
    a[i] = a[i + 1]
    j = 1
    while i + j + j < a[i]:
        if s[i] == s[i + j] and s[i] == s[i + j + j]:
            a[i] = i + j + j
        j += 1
    ans += n - a[i]
print(ans)
