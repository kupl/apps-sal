 
for i in range(eval(input())):
 n=eval(input())
 s=list(map(int,input().split()))
 f=0
 s1=0
 s2=0
 for j in range(0,n):
  s1=sum(s[0:j])
  s2=sum(s[j+1:n])
  
  if(s1 == s2):
   f=1
   print(j)
   break
 if(f==0):
  print("-1")
     

