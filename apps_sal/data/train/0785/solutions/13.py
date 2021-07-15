t = int(input())
while t!=0:
 a = int(input())
 give = 0
 take = 0
 m = []
 i = 1
 
 while(1):
  give+=2**(i-1)
  take+=a 
  
  if (take-give)<=0:
   break
  else:
   m.append(take-give)
   i+=1
   
 d2 = m.index(max(m)) + 1 
 d1 = len(m)
 
 print(d1,d2)
 # print(m)
 t-=1
