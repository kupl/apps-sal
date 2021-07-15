s=input()
if s[0]=='0' or s[-1]=='1' or s[:-1]!=s[:-1][::-1]:
    print(-1)
    return
e=[]
bi=0
for i,j in enumerate(s[:-1]):
    e.append([bi,i+1])
    if j=='1':
        bi=i+1
for i,j in e:
    print(i+1,j+1)
