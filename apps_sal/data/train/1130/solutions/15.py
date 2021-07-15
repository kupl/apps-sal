import math as m
T = int(input())
for i in range(T):
 N,V = (int(x) for x in input().split())
 ages=list(map(int,input().split(" ")))
 risk=[]
 notrisk=[]
 for i in ages:
  if i<=9 or i>=80:
   risk.append(i)
  else:
   notrisk.append(i)
 print(m.ceil(len(risk)/V)+m.ceil(len(notrisk)/V))
 
 
 

