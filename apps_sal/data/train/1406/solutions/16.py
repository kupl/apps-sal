t=int(input())
for i in range(t):
 num_to_bits =[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
 def countSetBitsRec(num):
  nibble = 0
  if(0 == num):
   return num_to_bits[0] 
  nibble = num & 0xf 
  return num_to_bits[nibble] + countSetBitsRec(num >> 4)
 n,q=input().split()
 n=int(n)
 q=int(q)
 A=[]
 A=list(map(int,input().split()))
 od=0
 ev=0
 for j in range(n):
  num=A[j]
  co=countSetBitsRec(num)
  if(co%2==0):
   ev+=1
  else:
   od+=1
 for j in range(q):
  p=int(input())
  co=countSetBitsRec(p)
  if(co%2==0):
   print(ev,end=' ')
   print(od)
  else:
   print(od,end=' ')
   print(ev)
