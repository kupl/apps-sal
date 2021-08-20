d = '  ZYXWVUTSRQPONMLKJIHGFEDCBA'
s = input().strip()
ans = 0
for i in s:
    ans += d.index(i)
print(ans)
