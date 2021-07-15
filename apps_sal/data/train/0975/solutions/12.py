# cook your dish here
T = int(input())
for t in range(T):
 s = input().split(' ')
 n = int(s[0])
 r = int(s[1])
 x = int(s[2])
 y = int(s[3])
 X = []
 Y = []
 if(x>0):
  s = input().split(' ')
 for i in range(x):
  X.append(int(s[i]))
 if(y>0):
  s = input().split(' ')
 for i in range(y):
  Y.append(int(s[i]))

 X = set(X)
 Y = set(Y)

 z = n - len(X.union(Y))
 if(z>=r):
  print(r)
 else:
  print(z)
