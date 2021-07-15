t = int(input())
for tt in range(t):
 n = int(input())
 arr = list(map(int, input().split()))
 ans = [1]*n
 for i in range(n-2, -1, -1):
  if (arr[i] < 0 and arr[i+1] > 0) or (arr[i] > 0 and arr[i+1] < 0):
   ans[i] = ans[i+1] + 1
 print(" ".join(map(str, ans)))

