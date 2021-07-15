def find(X,H):
 if len(X) == 2:
  return (X[1]-X[0])*(sum(H))
 
 X = sorted(X)
 W = []
 for i in range(1,len(H)-1):
  W += [X[i+1]-X[i-1]]
 W += [X[1]-X[0]]
 W += [X[-1]-X[-2]]
 W = sorted(W)
 H = sorted(H)
 return sum([W[i]*H[i] for i in range(len(W))])

for _ in range(int(input())):
 N = int(input())
 X = []
 H = []
 for i in range(N):
  x,h = list(map(int,input().strip().split()))
  X += [x]
  H += [h]
 print(find(X,H))
