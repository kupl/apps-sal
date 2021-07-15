# cook your dish here
try:
 for t in range(int(input())):
  x = int(input())
  count = -1
  if x % 10 == 0:
   count += 1
  elif x % 5 == 0:
   count = 1
  else:
   count = -1
  print(count)
except: pass
