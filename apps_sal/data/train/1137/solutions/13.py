# cook your dish here.
t=int(input())
for k in range(t):
 n=int(input())
 l=list(map(int,input().split()))
 i=0 
 j=n-1 
 l.sort()
 while(i<j):
  val=l[i]+l[j]
  if val==2000:
   print("Accepted")
   break
  elif val<2000:
   i+=1
  else:
   j-=1
 if i>=j:
  print("Rejected")
  

