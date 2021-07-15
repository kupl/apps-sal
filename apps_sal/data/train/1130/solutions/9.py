import math
for _ in range(int(input())):
 n,k=list(map(int,input().split()))
 l=list(map(int,input().split()))
 risk=0
 non_risk=0
 for i in range(len(l)):
  if(l[i]<=9 or l[i]>=80):
   risk+=1
  else:
   non_risk+=1
 print(math.ceil(risk/k)+math.ceil(non_risk/k))

