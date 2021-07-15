# cook your dish here
t=int(input())
for q in range(t):
 
 u=0
 nch=0
 ch,d,h=list(map(int,input().split()))
 l=sorted(list(map(int,input().split())))
 #print(l)
 for i in l:
  k=((i-1)//h)+1
  if k<3:
   
   u+=k
   #print(u)
   if u>d:
    break
   else:
    nch+=1
  else:
   break
 print(nch)
 #print(u)

