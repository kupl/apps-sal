for _ in range(int(input())):
 n, m = map(int, input().split())

 mLi = list(map(int, input().split()))
 nLi = [i for i in range(1, n + 1) if i not in mLi]
 x = []
 y = []
 for j in range(len(nLi)):
  if j % 2 == 0:
   x.append(nLi[j])
  else:
   y.append(nLi[j])
 
 print(*x, sep = " ")
 print(*y, sep = " ")
