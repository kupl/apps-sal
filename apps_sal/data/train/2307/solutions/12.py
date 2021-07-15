N,A,B=map(int,input().split())
X=list(map(int,input().split()))
dp = 0
for i in range(1, N):
  if A*(X[i]-X[i-1]) < B:
    dp += A*(X[i]-X[i-1])
  else:
    dp += B
print(dp)
