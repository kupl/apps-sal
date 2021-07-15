def Cook(N, K):
 if K == 1:
  return "NO"
 if (N//K)%K:
  return "YES"
 return "NO"

for T in range(int(input())):
 N, K = map(int,input().split())
 print(Cook(N, K))
