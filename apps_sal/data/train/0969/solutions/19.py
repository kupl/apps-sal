t=int(input())
while(t):
 t-=1
 # l1=[]
 laddus=0
 l1=input().split()
 n=int(l1[0])
 if(l1[1]=="INDIAN"):
  k=200
 else:
  k=400
 # print(k)    
 # for i in range(n):
 #     l2.append(input().split())
 while(n):
  n-=1
  l2=input().split()
  if(l2[0]=="TOP_CONTRIBUTOR"):
   laddus+=300
  elif(l2[0]=="CONTEST_HOSTED"):
   laddus+=50
  elif(l2[0]=="BUG_FOUND"):
   laddus+=int(l2[1])
  else:
   if(int(l2[1])<20):
    laddus+=300+20-int(l2[1])
   else:
    laddus+=300
 print(laddus//k) 
   
 # print(l2)
  

