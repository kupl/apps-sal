n,a,b=list(map(int,input().split()))
x=list(map(int,input().split()))
temp=0
for i in range(n-1):
    c=x[i+1]-x[i]
    temp+=min(c*a,b)
print(temp)

