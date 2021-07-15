import sys 
 
sys.setrecursionlimit(10**8) 
t=int(input())
m=[int(input()) for i in range(t)]

 
def rec(a,m,list1):

 b=a*m/(a-m)
 if b>=a and a*m%(a-m)==0 and a<=2*m:
  
  list1.append(a)
  a=a+1
  
  rec(a,m,list1)
  
 else:
  if a<=2*m:
   a=a+1
 
   rec(a,m,list1)
   
  
 
 
for i in m:
 c=0
 
 
 a=i+1
 ANS=[]
 rec(a,i,ANS)
 
 print(len(ANS))
 ANS.sort()
 for j in ANS:
  print(j)
    
   
    
    

