# cook your dish here
try:
 t=int(input())
 for i in range(t):
  l=int(input())
  a=[int(i) for i in input().split()]
  a.sort()
  if (len(a)>2):
   for i in range(l-1):
    p=len(a)
    d=(a[p-2]+a[p-1])/2
    del a[p-2]
    del a[p-2]
    a.append(d)
   print(a[0])
  else:
   t=sum(a)
   avg=t/len(a)
   print(avg)
except EOFError:
 pass
  
  

