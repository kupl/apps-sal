try:
 a,n,k=map(int,input().split())
 kList=[0 for i in range(k)]
 for i in range(k):
  kList[i]=a%(n+1)
  a=a//(n+1)
 print(*kList)
except:
 pass
