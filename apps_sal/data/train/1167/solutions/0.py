s = input().lower()
vow = ['a', 'e', 'i', 'o', 'u', 'y']
ans = ''
for ch in s:
    if ch in vow:
        continue
    if ch.isalpha():
        ans += '.' + ch
print(ans)
