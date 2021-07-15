# cook your dish here
a,n,k=map(int,input().split())
for i in range(k):
 print(a%(n+1),end=' ')
 a=a//(n+1)
 
