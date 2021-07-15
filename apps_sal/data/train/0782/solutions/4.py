t = int(input())

for i in range(t):
 n = int(input())
 cost = list(map(int, input().split()))
 w, y = list(map(int, input().split()))
 temp = w-y+1
 if temp<=0:
  print("Not Possible")
 else:
  cost.sort()
  total = temp*cost[0]
  for j in range(y-1):
   total+=cost[j+1]
  print(total)
   
  

