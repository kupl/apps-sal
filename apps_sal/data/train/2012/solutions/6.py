n=int(input())
if n%4==2 or n%4==3:
        print(-1);return
res,i=[0]*n,0
for i in range(0,n//2,2):
    res[i],res[i+1]=i+2,n-i
    res[n-i-1],res[n-i-2]=n-i-1,i+1
    i+=2
if n%4==1:res[n//2]=n//2+1
print(*res)
