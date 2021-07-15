t=int(input())
for i in range(t):
 n,a,b,k=list(map(int,input().split()))
 l=[]
 p1=[]
 p2=[]
 for i in range(1,n+1):
  if(i%a==0 and i%b!=0):
   p1.append(i)
  if(i%b==0 and i%a!=0):
   p2.append(i)
 if((len(p1)+len(p2))>=k):
  print("Win")
 else:
  print("Lose")
  
   
   

