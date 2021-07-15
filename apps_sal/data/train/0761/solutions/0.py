t=int(input())

def diffe(a,b):
 return int(a-b)

while t :
 t=t-1
 
 lia=[]
 lib=[]
 lik=[]
 lim=[]
 liab=[]
 likm=[]
 n,k,m=list(map(int,input().split()))
 
 
 lia=list(map(int,input().split()))
 lib=list(map(int,input().split()))
 lik=list(map(int,input().split()))
 lim=list(map(int,input().split()))
 liab=list(map(diffe,lia,lib)) 
 
 likm=lik+lim
 
 
 likm.sort()
 
 liab.sort()
 liab.reverse()
 
 for i in range(0,len(liab)): 
  for j in range(len(likm)-1,0-1,-1):
   a=likm.pop()
   if (liab[i]-a)>=0:
     liab[i]=liab[i]-a
     
     break
     
     
 print(sum(liab)) 


