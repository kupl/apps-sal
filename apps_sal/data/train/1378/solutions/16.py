# cook your dish here
a,n,k=input().split()
a,n,k=int(a),int(n),int(k)
klist=[0 for i in range(k)]
for i in range(k):
 klist[i]=a%(n+1)
 a=a//(n+1)
print(*klist)
