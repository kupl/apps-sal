for t in range(int(input())):
 string = input()
 n = len(string)
 if n == 1:
  print("NO")
 elif n == 2:
  if string[0] != string[1]:
   print("YES")
  else:
   print("NO")
 elif n > 2:
  first = string[0]
  second = string[1]

  if first == second:
   print("NO")
  else:
   flag = 1
   for i in range(2, n):
    if i % 2 != 0:
     if string[i] == second:
      flag = 1
     else:
      flag = 0
      break
    else:
     if string[i] == first:
      flag = 1
     else:
      flag = 0
      break
  if flag == 1 and n == 3:
   print("NO")
  elif flag == 1:
   print("YES")
  else:
   print("NO")
