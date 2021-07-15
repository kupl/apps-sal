s=input()
l,r=[],[]
for x in range(len(s)):
    if s[x]=='r':
        r.append(x+1)
    else:
        l.append(x+1)
for el in r:
    print(el)
for el in l[::-1]:
    print(el)
