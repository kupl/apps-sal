n=int(input())
a=list()
for i in range(n):
    a.append(list(map(int,input().split())))
c=0
for i in range(n):
    for j in range(i+1,n):
        if a[i][1]+a[j][1]==0:
            c+=1
            print('YES')
            break
    if c!=0:
        break
if c==0:
    print("NO")
