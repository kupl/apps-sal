s = list(map(str, input().split()))
res = min(s, key=len)
for i in range(len(s)):
    print(res, s[i], end=' ')
print(res)
