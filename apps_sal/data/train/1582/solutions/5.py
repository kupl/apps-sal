# cook your dish here
n = int(input())
s = input()
s = list(s)
ans = 0
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        ans += 1

print(ans)
