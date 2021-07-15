from sys import stdin
t=(stdin.readline())
levels=[0]*101
for i in range(int(t)):
   sochef=0
   warriors = stdin.readline()
   n,m = warriors.split()
   for i in range(int(n)):
      x=stdin.readline()
      c,l=x.split()
      levels[int(l)]+=int(c)
   for i in range(int(m)):
      x=stdin.readline()
      c,l=x.split()
      levels[int(l)]-=int(c)
   for i in range(101):
      if levels[i]<0:
         sochef+=levels[i]
      levels[i] = 0
   print(abs(sochef))

