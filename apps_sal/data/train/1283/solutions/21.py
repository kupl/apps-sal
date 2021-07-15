# cook your dish here
import math
t=int(input())
for i in range(0,t):
    n=int(input())
    p=[]
    for j in range (2,n+1):
        if j==2:
            p.append(j)
        else:
            f=0
            for k in range(2,int(math.sqrt(j)+1)):
                if(j%k==0):
                    f=1
                    break
            if f==0:
                p.append(j)
    ar=[]
    for j in range(0,len(p)-1):
        for k in range(j+1,len(p)):
            if(p[j]*p[k]<n):
                ar.append(p[j]*p[k])
    f=0
    for j in range(0,len(ar)):
        if ((ar[j]*2==n)or (n-ar[j] in ar)):
            print('YES')
            f=1
            break
    if f==0:
        print('NO')
                
