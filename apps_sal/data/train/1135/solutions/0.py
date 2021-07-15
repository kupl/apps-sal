# cook your dish here
t=int(input())
while t!=0:
 n,k=map(int,input().split())
 lst=[]
 for i in range(1,n+1):
  lst.append(i)
 lst[k],lst[n-1]=lst[n-1],lst[k]
 for item in lst:
  print(item,end=' ')
 t-=1
