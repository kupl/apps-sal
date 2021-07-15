# cook your dish here
t = int(input())
for _ in range(t):
 n = int(input())
 a = input()
 b = input()
 a = list(a)
 b = list(b)
 l = []
 f = 1
 for i in range(n):
  if b[i]!=a[i]:
   if b[i] in a and b[i]<a[i]:
    l.append(b[i])
   else:
    f = 0
    break
 if f==0:
  print(-1)
 else:
  if l == []:
   print(0)
  else:
   l = sorted(list(set(l)), reverse = True)
   print(len(l))
   for i in range(len(l)):
    Q=[]
    R=[]
    for j in range(len(a)):
     if b[j]==l[i]:
      Q.append(j)
      R.append(a[j])
    if l[i] not in R:
     for k in range(n):
      if a[k]==l[i]:
       Q.append(k)
       break
    print(len(Q),*Q)
