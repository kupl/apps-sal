n=int(input())
b=[]
for i in range(0,n):
    a=input()
    b.append(a)
ans=0
for j in range(0,7):
    count=0
    for i in range(0,n):
        if b[i][j]=='1':
            count+=1
    ans=max(ans,count)
print(ans)

