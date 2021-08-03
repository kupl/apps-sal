s = input()
p = True
if s[0] == 'h':
    s1 = 'http://'
    x = 7
else:
    s1 = 'ftp://'
    x = 6
for i in range(len(s1) - 3, len(s)):
    if s[i:i + 2] == 'ru' and p and len(s1) != x:
        s1 += '.'
        p = False
    if s1[-3:] == '.ru':
        s1 += '/'
    s1 += s[i]
print(s1)
