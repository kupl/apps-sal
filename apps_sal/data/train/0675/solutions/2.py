from math import log2
t=int(input())
for _ in range(t):
 n=int(input())
 s1=""
 #print(log2(n))
 if n>1 and log2(n)==int(log2(n)):
  print(-1)
 else:
  #print(3)
  f=[0]*n
  s=n//2
  if n==1:
   s=1
  f[s-1]=1
  s1+="{} ".format(s)
  #print(s1)
  while f!=[1]*n:
   for i in range(n):
    if f[i]==0 and s&(i+1)>0:
     s=i+1
     s1+="{} ".format(s)
     f[s-1]=1
     break
    #print(f,"000000000000")
   #(f)    
  print(s1) 

