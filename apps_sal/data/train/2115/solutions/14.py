def findIndex(x,L,R,T):
    if x[R]<T:
        return R
    if x[L]>=T:
        return L
    while R-L>1:  
        M=(R+L)//2
        if x[M]>=T:
            R=M
        else:
            L=M
    return R
        

n,d=[int(i) for i in input().split()]
x=[int(i) for i in input().split()]
ans=0
for R in range(2,n)[::-1]:
    L=findIndex(x,0,R,x[R]-d)
    ans+=(R-L)*(R-L-1)//2
print(ans)
