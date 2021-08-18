n = input().strip().replace(" ", "")
ans = 0
for i in n:
    ans += 92 - ord(i)
print(ans)
