n, k = list(map(int, input().split()))

arr = [True for i in range(n)]

open = 0

for i in range(k):
 temp = input().split()
 if temp[0] == "CLICK":
  cl = int(temp[1])-1
  if arr[cl]:
   open += 1
   arr[cl] = False
  else:
   open -= 1
   arr[cl] = True
   
 else:
  open = 0
  arr = [True for i in range(n)]
 print(open)
