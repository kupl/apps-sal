for _ in range(int(input())):
 D = int(input())
 P = 10 ** 5 - 2
 a = []
 if D == 0:
  print("1")
  print("1")
 else:
  while D > 0:
   P = min(P, D)
   a.append(P + 1)
   a.append(P + 2)
   a.append(1)
   D = D - P
  print(len(a))
  print(*a)
