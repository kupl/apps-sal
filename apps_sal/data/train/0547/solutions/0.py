import sys

t = int(input())

def g(a,b):
 if (a > b):
  tmp = a
  a = b
  b = tmp
 if (b == a):
  return 0
 if (b % a == 0):
  return int(b/a)-1
 r = g(b%a,a)
 q = int(b/a)
 if (r >= q):
  return q-1
 else:
  return q

def mex(x):
 n = len(list(x.keys()))
 for i in range(n):
  if (i not in x):
   return i
 return i

def g2(a,b):
 if (a == b):
  return 0
 if (a > b):
  tmp = a
  a = b
  b = tmp
 if (b % a == 0):
  return int(b/a)-1
 q = int(b/a)
 x = {}
 r = b % a
 for i in range(q):
  x[g2(r+i*a,a)] = True
 return mex(x)

#print(str(g(6,33))+" "+str(g2(6,33)))

while (t):

 n = int(input())
 x = 0
 while (n):
  line = input().split()
  a = int(line[0])
  b = int(line[1])
  x ^= g(a,b)
  n -= 1
 if (x):
  sys.stdout.write("YES\n")
 else:
  sys.stdout.write("NO\n")
 #print(str(g(a,b)) + " " + str(g2(a,b)))
 t -= 1
