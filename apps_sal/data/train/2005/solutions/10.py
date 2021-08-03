s = input()
cur, ans = - 1, 0
for i in range(len(s)):
    for j in range(cur + 1, i - 1):
        if (i + j) % 2 == 0 and s[i] == s[j] and s[i] == s[(i + j) // 2]:
            cur = j
    ans += cur + 1
print(ans)
