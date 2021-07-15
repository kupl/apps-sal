for _ in range(int(input())):
 N,k=map(int,input().split())
 A=list(map(int,input().split()))
 B=""
 for i in range(N):
  if A[i]%k==0:
   B+="1"
  else:
   B+="0"
 print(B)
