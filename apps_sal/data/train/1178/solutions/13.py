for _ in range(int(input())):
 n=int(input())
 ar=[int(x) for x in input().split()]
 ar.sort()
 s=0
 an=0
 for i in range(n):
  if ar[i]<=s:
   s+=1
   an+=1
  else:
   break
 print(an)
   

