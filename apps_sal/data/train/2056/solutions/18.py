n = int(input())
s = list(input())
s1 = input()
ans = 0
for i in range(n):
    if s[i] != s1[i]:
        if i != n - 1 and s[i] != s[i + 1] and (s1[i + 1] != s1[i]):
            s[i] = s1[i]
            s[i + 1] = s1[i + 1]
        else:
            s[i] = s1[i]
        ans += 1
print(ans)
