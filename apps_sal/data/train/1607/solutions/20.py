s = input()
a = 0
q = 0
ans = 0
for c in s:
    if c == 'Q':
        ans += a
        q += 1
    if c == 'A':
        a += q
print(ans)
