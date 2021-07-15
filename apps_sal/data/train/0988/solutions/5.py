t = int(input())
for _ in range(t):
 n = int(input())
 l = list(map(int,input().split()))
 #print(l)
 
 s = max(l)
 s = bin(s)
 maxbits = len(s)-1
 x = []
 for i in range(maxbits+1):
  count = 0
  for j in range(n):
   if ((2**i)&l[j])==2**i:
    count+=1 
  
  
   
  if count>n//2:
   x.append(1)
  else:
   x.append(0)
 x.reverse() 
 ans = ''
 
 for i in x:
  ans+=str(i)
 ans1 = int(ans,2)
 #print(ans1)
 sm=0
 for i in l:
  sm+=(i^ans1)
 print(sm)
  
 

