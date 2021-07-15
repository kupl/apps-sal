T = int(input())
for _ in range(T):
 n = int(input())
 arr = list(map(int, input().split()))
 values = []
 if len(arr) == 1:
  print(0)
 else:
  for i in range(1, len(arr)):
   star = 0
   for j in range(i):
    if arr[j]%arr[i] == 0:
     star += 1
   values.append(star)
  print(max(values))
