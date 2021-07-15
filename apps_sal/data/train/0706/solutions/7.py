for _ in range(int(input())):
 n,k = list(map(int,input().split()))
 s = 0
 res = 0
 for i in map(int,input().split()):
  if i>k:
   res=-1
   s=0
   break
  if s+i<=k:
   s+=i
  else:
   s=i
   res+=1
 if s>0: res+=1
 print(res)

