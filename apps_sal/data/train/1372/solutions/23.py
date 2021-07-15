t = int(input())
for x in range(t):
 a = [int(x) for x in input().split()]
 d1 = (a[0]**2 + a[1]**2)**0.5
 d2 = (a[2] ** 2 + a[2] ** 2) ** 0.5

 if d1 < d2:
  print("A IS CLOSER")
 else:
  print("B IS CLOSER")
