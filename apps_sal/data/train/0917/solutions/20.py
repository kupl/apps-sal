t = int(input())
for _ in range(t):
 n, k = [int(i) for i in input().split()]
 arr = [int(i) for i in input().split()]
 list_diff = []
 for i in range(n):
  for j in range(i+1, n):
   list_diff.append(abs(arr[i]+arr[j]-k))
 m = min(list_diff)
 ans = list_diff.count(m)
 print(m, end=" ")
 print(ans)

