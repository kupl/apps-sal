for _ in range(int(input())):
 N = int(input())
 A=list(map(int, input().split()))
 A.sort()
 k=0
 for i in range(len(A)):
  if A[i]<=k:
   k+=1
  else:
   pass
 print(k)
