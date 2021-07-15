t = int(input())
for _ in range(t):
 n, s = map(int, input().split())
 p = list(map(int, input().split()))
 arr = list(map(int, input().split()))
 min_def = 9999999
 min_for = 9999999
 for i in range(n):
  if arr[i] == 0:
   if p[i] < min_def:
    min_def = p[i]
  else:
   if p[i] < min_for:
    min_for = p[i]
 if s + min_def + min_for <= 100:
  print('yes')
 else:
  print('no')
