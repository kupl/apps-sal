# cook your dish here
for _ in range(int(input())):
 n=int(input())
 ar=list(map(int,input().split()))
 odd=0
 even=0
 if n==1:
  print(0)
  continue
 for i in range(n):
  if ar[i]%2==1:
   odd+=1
  else:
   even+=1
 if odd>0:
  vo=(odd-1)*2+even
 else:
  vo=even
 if even>0:
  ve=(even-1)*2+odd
 else:
  ve=odd
 print(min(vo,ve))

