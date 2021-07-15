n,m = list(map(int,input().split()))
N = list(map(int,input().split()))
P1 = []
p1 = []
P2 = []
p2 = []
for i in range(m):
 X1,X2,X3 = list(map(str,input().split()))
 X = []
 X.append(int(X1))
 X.append(int(X2))
 X.append(X3)
 if int(X[0]) in N:
  P1.append(X)
  p1.append(int(X[1]))
 else:
  P2.append(X)
  p2.append(int(X[1]))
 x = []

p1.sort(reverse=True)
p2.sort(reverse=True)

for x in range(len(p1)):
 for xx in range(len(P1)):
  if int(P1[xx][1]) == int(p1[x]):
   print(P1[xx][2])
   del P1[xx]
   break

for x in range(len(p2)):
 for xx in range(len(P2)):
  if int(P2[xx][1]) == int(p2[x]):
   print(P2[xx][2])
   del P2[xx]
   break
