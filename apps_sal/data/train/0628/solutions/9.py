# cook your dish here
t = int(input())

for i in range(t):
 l = list(input())
 n = len(l)
 p = l.index('W')
 left = p
 right = n-p-1
 if(left^right == 0):
  print("Chef")
 else:
  print("Aleksa")
