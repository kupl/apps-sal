import sys
n=input()
i=0
n=n+'a'
m=""
while n[i]=='a' and len(n)>i+1:
    i+=1
    m=m+'a'
if i+1==len(n):
    w=m[0:len(m)-1]+'z'
    print(w)
    return
while n[i]!='a' and len(n)>i:
    m=m+chr(ord(n[i])-1)
    i+=1
m=m+n[i:len(n)-1]

print(m)

