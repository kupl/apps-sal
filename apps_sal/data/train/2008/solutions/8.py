from sys import stdin
n=int(stdin.readline().strip())
s=list(map(int,stdin.readline().strip().split()))

l=0
flag=True
x=0
for i in range(1,n):
    if s[i]!=s[i-1]:
        if flag:
            flag=False
            l=i-1
    else:
        r=i-1
        if not flag:
            y=0
            yy=r-1
            for j in range(l+1,r):
                s[j]=s[j-1]
                y+=1
                s[yy]=s[yy+1]
                yy-=1
                if(yy<=j):
                    break
            x=max(x,y)
        flag=True

if True:
    if True:
        if not flag:
            y=0
            yy=n-2
            r=n-1
            for j in range(l+1,r):
                s[j]=s[j-1]
                y+=1

                s[yy]=s[yy+1]
                yy-=1
                if(yy<=j):
                    break
            x=max(x,y)
print(x)
print(*s)


