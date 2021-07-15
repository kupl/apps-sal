t=int(input())
for _ in range(t):
 n,z1,z2=map(int,input().split())
 l = list(map(int,input().split()))
 if z1 in l or z2 in l or -1*z1 in l or -1*z2 in l:
  print(1)
  continue
 if z1==0 and z2==0:
  print(2)
  continue
 l=list(map(abs,l))
 for i in l:
  if abs(z1-i) not in l and abs(z2-i) not in l:
   print(0)
   break
  if abs(z1+i) not in l and abs(z2+i) not in l:
   print(0)
   break
 else:
  print(2)
