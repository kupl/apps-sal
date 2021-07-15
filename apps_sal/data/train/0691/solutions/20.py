for _ in range(int(input())):
 N=int(input())
 a=list(map(int,input().split()))
 maxx=0
 for index,items in enumerate(a):
  k=0
  for i in range(index):
   if a[i]%items==0:
    k+=1
  maxx=max(k,maxx)
 print(maxx)
