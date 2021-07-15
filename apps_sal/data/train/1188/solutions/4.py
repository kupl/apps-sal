n=eval(input())
l=list(map(int, input().split()))
z=[0 for i in range(n+1)]
for i in range(n):z[l[i]]=1
for i in range(n+1):
 if z[i]==0:print(i, end=' ')
print()
