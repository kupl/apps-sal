from itertools import permutations
a = [int(num) for num in input().split()]

l = list(permutations(a))
flag = False
for e in l:
 e0 = float(e[0])
 e1 = float(e[1])
 e2 = float(e[2])
 e3 = float(e[3])
 if e0 / e1 == e2 / e3:
  print("Possible")
  flag = True
  break
if flag == False:
 print("Impossible")
