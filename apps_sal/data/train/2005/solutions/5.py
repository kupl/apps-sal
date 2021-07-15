s = input()

n = len(s)

ans = 0
l = 0

for i in range(0, n):
    for j in range(i - 1, l, -1):
        if 2 * j - i < l:
            break
        if s[i] == s[j] == s[j + j - i]:
             ans += ((2 * j - i) - l + 1) * (n - i)
             l = (2 * j - i + 1)	

print(ans)
