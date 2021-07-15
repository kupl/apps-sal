t=int(input())
f=[]
for i in range(t):
    a,b,c,d=map(int,input().split())
    if abs(c-d)==0 and a==b:
        f.append('YES')
        continue
    if abs(c-d)==0 and a!=b:
        f.append('NO')
        continue
    if a==b:
        f.append('YES')
    elif abs(a-b)%abs(c-d)==0:
        f.append('YES')
    elif abs(a-b)%abs(c-d)!=0:
        f.append('NO')
for i in range(t):
    print(*f[i],sep='')

