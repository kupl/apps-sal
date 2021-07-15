j = 0
for _ in range(int(input())) :
 m, n = map(int, input().split())
 rx, ry = map(int, input().split())
 l = int(input())
 s = input()
 x = 0
 y = 0
 for i in range(l) :
  if s[i] == "U" :
   y += 1
  elif s[i] == "D" :
   y -= 1
  elif s[i] == "L":
   x -= 1
  elif s[i] == "R":
   x += 1
 j = j + 1
 print('Case '+ str(j) + ': ', end = "")
 if x == rx and y == ry :
  print("REACHED")
 elif x < 0 or x > rx :
  print("DANGER")
 elif y < 0 or y > ry :
  print("DANGER")
 else :
  print("SOMEWHERE")
