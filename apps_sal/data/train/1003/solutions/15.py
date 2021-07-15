t=int(input())
levels=[0]*101
for i in range(t):
   sochef=0
   warriors = input()
   n,m = warriors.split()
   for i in range(int(n)):
      x=input()
      c,l=x.split()
      levels[int(l)]+=int(c)
   for i in range(int(m)):
      x=input()
      c,l=x.split()
      levels[int(l)]-=int(c)
   for i in range(101):
      if levels[i]<0:
         sochef+=levels[i]
      levels[i] = 0
   print(abs(sochef))

