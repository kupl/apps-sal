for _ in range(int(input())):
 n=int(input())
 L=list(map(int,input().split()))
 R=list(map(int,input().split()))
 pos=0
 Rmax=R[0]
 maxx=0
 for i in range(n):
  temp=L[i]*R[i]
  
  if temp>maxx:
   maxx=temp
   Rmax=R[i]
   pos=i
   
  elif temp==maxx:
   if R[i]>Rmax:
    Rmax=R[i]
    pos=i
 print(pos+1)
     
     
  

