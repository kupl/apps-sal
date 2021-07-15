s = input()
res = []
for i in range(len(s)):
    if s[i] == 'r':
        res.append(str(i+1))
for i in range(len(s)-1, -1, -1):
    if s[i] == 'l':
        res.append(str(i+1))
print('\n'.join(res)) 

