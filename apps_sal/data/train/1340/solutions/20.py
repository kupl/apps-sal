for _ in range(int(input())):
 n = int(input())
 arr = list(map(int, input().split()))
 arr.insert(0,9)
 ans = m = 0
 for i in range(1, n+1):
  if arr[i] >= 0:
   m += 1
   ans += arr[i]
 sub = []
 for i in range(1, m+1):
  if arr[i] < 0:
   sub.append(i)
 for i in range(m+1, n+1):
  if arr[i] >= 0:
   sub.append(i)
 if ans == 0:
  print(ans)
  print(ans)
 else:
  print(ans)
  print(len(sub),*sub)
