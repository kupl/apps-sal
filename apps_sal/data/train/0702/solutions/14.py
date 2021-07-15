import math
t_c = int(input())
for _ in range(t_c):
 m, tc, th = [int(x) for x in input().split(" ")]
 temp = (th-tc)/3
 if len(str(temp).split(".")[1]) <= 5:
  if math.ceil(temp) <= m:
   print("No")
  else:
   print("Yes")
 else:
  print("Yes")

