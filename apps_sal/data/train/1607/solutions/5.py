s = input()
ans = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == 'Q' and s[j] == 'A':
            ans += s[j + 1:].count('Q')
print(ans)

