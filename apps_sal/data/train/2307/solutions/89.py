n,a,b=map(int,input().split())
x=list(map(int,input().split()))
print(sum([min(x[i+1]*a-x[i]*a,b)for i in range(n-1)]))
