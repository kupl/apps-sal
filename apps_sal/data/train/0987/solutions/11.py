from math import sqrt
for _ in range(int(input())) :
 s1, s2, a2, v = map(int, input().split())
 t1 = s1 / v
 t2 = sqrt((2 * (s1 + s2)) / a2)
 if t1 < t2 :
  print("Bolt")
 else :
  print("Tiger")
