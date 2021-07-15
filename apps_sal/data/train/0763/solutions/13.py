t = int(input())
while t != 0:
 n = int(input())
 s = input()
 p = input()
 f = 1
 o = 0
 z = 0
 for j in range(n):
  if s[j] != p[j]:
   if s[j] == "1":
    o += 1
   else:
    z += 1
   if o < z:
    f = 0
    break
 if f == 1 and o == z:
  print("Yes")
 else:
  print("No")
 t = t-1

