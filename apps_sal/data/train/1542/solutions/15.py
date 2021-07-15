
t = int(input())
maxi =[]
for _ in range(t):
 n = int(input())
 board = input()
 arr = input()
 points = list(map(int , arr.split(' ')))
 values = []
 for i in range(n-7):
  dw = 1
  tw = 1
  total = 0 
  for j in range(i,i+8):
   if board[j] == 'd':
    total += 2*points[j-i]
   elif board[j] == 't':
    total += 3*points[j-i]
   elif board[j] == 'D':
    dw *= 2
    total += points[j-i]
   elif board[j] == 'T':
    tw *= 3
    total += points[j-i]
   elif board[j] == "." :
    total += points[j-i]
   #print(total)
  
  total *= dw
  
  total *= tw 
  values.append(total)
 #print(values)
 maxi.append(max(values))
for element in maxi:
 print(element)


