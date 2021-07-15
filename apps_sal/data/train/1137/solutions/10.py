for t in range(int(input())):
 n = int(input())
 A = [int(i) for i in input().split()]
 A.sort()
 X = 2000
 i=0
 j=n-1
 ans = 0
 while i<j:
  if A[i] + A[j] == X:
   ans=1
   break
  elif A[i] + A[j] < X:
   i+=1
  else:
   j-=1
 if ans==1:
  print("Accepted")
 else:
  print("Rejected")

