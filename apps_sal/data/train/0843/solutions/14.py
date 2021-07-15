testCases = int(input())
lines = 0
for _ in range(testCases):
 lines = int(input())
 arr = []
 for _ in range(lines):
  arr.append(sorted(list(map(int,input().split())),reverse=True))

 maximum = max(arr[lines-1])
 choosen = maximum
 bool = True
 for index in range(lines-2,-1,-1):
  secondBool = True
  for j in range(lines):
   if arr[index][j] < maximum:
    choosen += arr[index][j]
    maximum = arr[index][j]
    secondBool = False
    break
  if secondBool == True:
   bool = False
   break
 if bool == True:
  print(choosen)
 else:
  print(-1)

