MOD=1000000007
levels,q=input().split()
levels=int(levels)
q=int(q)
left=levels+1
right=levels+1
top=1
bottom=pow(2,levels)
edges=0
f=1
for i in range(1,levels+1):
 f=((2%MOD)*(f%MOD))%MOD
 edges+=f

levels+=1

for i in range(1,q+1):
 l1=list(map(int,input().split()))
 if(l1[0]==1):
  y=l1[1]
  if(y==1):
   edges=((edges%MOD)*(2%MOD))%MOD
   edges=((edges%MOD)+(levels%MOD))%MOD
   top=((top%MOD)*(2%MOD))%MOD
   bottom=((bottom%MOD)*(2%MOD))%MOD
  elif(y==2):
   edges=((edges%MOD)*(2%MOD))%MOD
   edges=((edges%MOD)+(levels%MOD))%MOD
   top=((top%MOD)*(2%MOD))%MOD
   bottom=((bottom%MOD)*(2%MOD))%MOD
  elif(y==3):
    edges=((edges%MOD)*(2%MOD))%MOD
    edges=((edges%MOD)+(top%MOD))%MOD
    top=bottom;
    levels=((levels%MOD)*(2%MOD))
  elif(y==4):
   edges=((edges%MOD)*(2%MOD))%MOD
   edges=((edges%MOD)+(bottom%MOD))%MOD
   bottom=top
   levels=((levels%MOD)*(2%MOD))
 elif(l1[0]==2):
  print(edges%MOD)

