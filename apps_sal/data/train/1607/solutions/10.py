s = input()
n = len(s)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if s[i] == s[k] == 'Q' and s[j] == 'A':
                ans += 1
print(ans)
