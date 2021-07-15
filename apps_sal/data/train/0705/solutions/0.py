ar = []
ar.append(1)
for i in range(1, 31):
 ar.append(ar[i-1]*(4*i-2)/(i+1))
t = int(input())
while(t>0):
 n = int(input())
 if(n==0):
  print(0)
 else:
  print(ar[n]*2)
 t=t-1

