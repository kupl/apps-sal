t = eval(input())
for i in range(0,t):
  ar = list(map(int , input().split()))
  arr = list(map(int , input().split()))
  count = 0
  for j in range(0, ar[1]):
    z = 1<<j
    if z not in arr :
      count+=1
  print(count)

