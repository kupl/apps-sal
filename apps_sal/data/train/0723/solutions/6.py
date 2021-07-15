from sys import stdin

T = int(stdin.readline().strip())
for x in range(T):
 N = int(stdin.readline().strip())
 ansList = []
 for i in range(N):
  a, p = list(map(int, stdin.readline().strip().split()))
  if p > 1:
   ansList.append("%dx^%d" % (a*p, (p-1)))
  elif p == 1:
   ansList.append("%d" % (a*p))
 value = True
 ans = 0
 for k in range(ansList.__len__()):
  if not "x" in ansList[k]:
   ans += int(ansList[k])
   continue
  else:
   value = False
 if value:
  print(ans)
  continue
 for j in range(ansList.__len__()):
  if j != ansList.__len__() - 1:
   print(ansList[j], "+", end=' ')
  else:
   print(ansList[j])

