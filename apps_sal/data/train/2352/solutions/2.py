s = input()
out = ''
l = 0
if s.startswith('http'):
    out += 'http://'
    l = 4
else:
    out += 'ftp://'
    l = 3
r = s.index('ru')
if r == l:
    r = s.index('ru', r + 2, len(s) - 1)
out += s[l:r] + '.ru'
if r + 2 != len(s):
    out += '/' + s[r + 2:]
print(out)
