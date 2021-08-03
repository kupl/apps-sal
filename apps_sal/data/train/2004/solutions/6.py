s = input()
c = {'0': 0, '1': 0}
for i in range(len(s)):
    c[s[i]] += 1
if c['0'] == 0:
    print(s[1:])
else:
    out = ''
    x = s.index('0')
    print(s[:x] + s[x + 1:])
