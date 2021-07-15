import sys

def shl(s, be, en):
    t = s[:be];
    for i in range(be, en):
        if s[i]=='a':
            t += 'z'
        else:
            t += chr(ord(s[i])-1)
    return t+s[en:]

s = input()
i = 0
L = len(s)
while i<L and s[i]=='a':
    i += 1
if i==L:
    print(s[:L-1]+'z')
    return
    
j = i+1
while j<L and s[j]!='a':
    j += 1
print(shl(s,i,j))

