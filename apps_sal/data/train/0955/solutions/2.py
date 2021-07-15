import math
MAX = 10001
PRIME=[]
A=[1 for i in range(MAX)]
A[0] = 0
A[1] = 0
B=[0 for i in range(MAX)]

for i in range(2,int(math.sqrt(MAX))+1):
 if A[i] is 1:
  for j in range(i*i,MAX,i):
   A[j] = 0
for i in range(MAX):
 if A[i] is 1:
  PRIME.append(i)

for p in PRIME:
 for q in PRIME:
  if p+(2*q)>=MAX:
   break
  B[p+(2*q)]+=1

for _ in range(int(input())):
 n=int(input())
 print(B[n])

  
  

