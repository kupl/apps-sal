n,a,b,*X=map(int,open(c:=0).read().split())
for i in range(n-1):c+=min(a*(X[i+1]-X[i]),b)
print(c)
