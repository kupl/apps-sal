# cook your dish here
a,n,k=list(map(int,input().split()))

l=[]
for i in range(0,k):
 l.append(a%(n+1))
 a=a//(n+1)
for i in l:
 print(i,end=" ")
print('')
