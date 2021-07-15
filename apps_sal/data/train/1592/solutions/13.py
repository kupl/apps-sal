for _ in range(int(input())):
 chef=0
 f=[]
 for j in range(int(input())):
  k=list(map(int,input().split()))
  for r in range(1,k[0]//2 +1 ):
    chef+=k[r]
  if(k[0]%2==1):
   f.append(k[k[0]//2 +1])
 f.sort(reverse=True)
 for p in range(0,len(f),2):
  chef+=f[p]
 print(chef)
   

