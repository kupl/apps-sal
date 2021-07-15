t = int(input())

def numOfCordinates(arr, raw_arr, r, c):
 num = 0
 possibleCords = [[r-1, c], [r+1,c], [r, c+1], [r, c-1]]
 
 for cords in possibleCords:
  if cords in raw_arr:
   num+=1
 
 return num
 

for _ in range(1,t + 1):
 
 (r,c) = map(int, input().split(" "))
 
 arr = []
 for i in range(r):
  ri = list(map(int, input().split(" ")))[:c]
  arr.append(ri)
 

 raw_arr = []
 for ri in range(r):
  
  for ci in range(c):
   raw_arr.append([ri,ci])
  

 for r in range(len(arr)):
  
  for c in range(len(arr[r])):
   no_cords = numOfCordinates(arr, raw_arr, r, c) 
   
   if no_cords == -1:
    arr[r][c] = -1
   
   elif arr[r][c] < no_cords:
    arr[r][c] = 0
   
   else:
    arr[r][c] = -1
 
 
 s = 0
 for ls in arr:
  s += sum(ls)
  
 if s==0:
  print("Stable")
 else:
  print("Unstable")
