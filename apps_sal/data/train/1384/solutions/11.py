num = int(input())

t=0
while(t<num):
 n,k = list(map(int,input().split()))
 s = str(input())

 count=0

 pos=[]
 for i in range(n):
  if(s[i]=="0"):
   pos.append(i)
 
 for i in range(len(pos)):
  ind = pos[i]
  val=0

  if(ind-k+1<0):
   val+=ind+1
  else:
   val+=k
   bn=ind-k
   while(bn>=0):
    if(s[bn]=="1"):
     val+=1
    else:
     break
    bn-=1
  if(i!=len(pos)-1):
   val+= pos[i+1]-pos[i]-1
  else:
   ui=0
   gh=pos[len(pos)-1]+1
   while(gh<n):
    if(s[gh]=="1"):
     ui+=1
    gh+=1
   val+=ui
  
  if(val>count):
   count=val
 if(len(pos)==0):
  print(n)
 else:
  print(count)
 t+=1



  

