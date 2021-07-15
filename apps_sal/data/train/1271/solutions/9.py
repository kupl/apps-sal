from collections import Counter


a= int(input())
while a!=0:
 b = int(input())
 original = list()
 original.append(0)
 ev,od=0,0

 for i in range(b):

  c = int(input())
  if c in original:
   print(ev,od)
   continue
  else:
   for j in range(len(original)):
    p = c^original[j]
    if Counter(bin(p))['1']%2 == 0:
     ev+=1
    else:
     od+=1
    original.append(p)
   print(ev,od)
  

 a-=1

