for _ in range(int(input())):
 n=int(input())
 arr = list(map(int,input().split()))
 X = int(input())
 if n==1:
  print(1,0)
  continue
 l,r = 0,n-1
 a,b=0,0
 sumA,sumB=0,0
 while l<r:
  if sumA<=sumB*X:
   sumA+=arr[l]
   l+=1
   a+=1
  else:
   sumB+=arr[r]
   r-=1
   b+=1
 if l==r:
  if sumA-sumB*X==0:
   if a>=b:
    a+=1
   else:
    b+=1
  elif sumA-sumB*X<0:
   a+=1
  else:
   b+=1
 print(a,b)

