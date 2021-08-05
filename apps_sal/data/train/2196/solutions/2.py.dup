n, m = list(map(int, input().split()))
s = input()
p = c = 0
for i in range(1, n):
    if s[i] == s[i - 1]:
        c += n * (m - 1)
        p = i
    elif s[i] != s[i - 2]:
        p = i - 1
    c += i - p
ans = n * n * (m - 1) - c
print(ans)
