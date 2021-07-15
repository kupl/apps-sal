t = int (eval(input()))

while t > 0:
 t -= 1
 r, c, m, j, k = list(map (int, input().split()))
 area = r * c
 if m + j + k != area:
  print("No")
  continue
 l = r
 b = c
 if m % l == 0:
  b -= m/l
  if b > 0 and (j % l == 0 or j % b == 0 or k %l == 0 or k % b == 0):
   print("Yes")
   continue
 l = r
 b = c
 if m % b == 0:
  l -= m/b
  if l > 0 and (j % l == 0 or j % b == 0 or k %l == 0 or k % b == 0):
   print("Yes")
   continue
 
 l = r
 b = c
 if j % l == 0:
  b -= j/l
  if b > 0 and (m % l == 0 or m % b == 0 or k %l == 0 or k % b == 0):
   print("Yes")
   continue
 l = r
 b = c
 if j % b == 0:
  l -= j/b
  if l > 0 and (m % l == 0 or m % b == 0 or k %l == 0 or k % b == 0):
   print("Yes")
   continue
 
 l = r
 b = c
 if k % l == 0:
  b -= k/l
  if b > 0 and (j % l == 0 or j % b == 0 or m %l == 0 or m % b == 0):
   print("Yes")
   continue
 l = r
 b = c
 if k % b == 0:
  l -= k/b
  if l > 0 and (j % l == 0 or j % b == 0 or m % l == 0 or m % b == 0):
   print("Yes")
   continue
 
 print("No")

